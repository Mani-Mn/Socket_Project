import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime


class ChatClient:
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        self.username = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setup_gui()
        self.connect_to_server()

    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("پیام‌رسان پیشرفته")

        # تنظیمات فونت فارسی
        self.font = ("Tahoma", 12)

        # چت باکس
        self.chat_box = scrolledtext.ScrolledText(self.root, font=self.font, width=50, height=20)
        self.chat_box.pack(padx=10, pady=10)
        self.chat_box.config(state='disabled')

        # فریم پایینی
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(pady=10)

        # ورودی پیام
        self.msg_entry = tk.Entry(bottom_frame, font=self.font, width=40)
        self.msg_entry.pack(side=tk.LEFT, padx=5)
        self.msg_entry.bind("<Return>", self.send_message)

        # دکمه ارسال
        send_btn = tk.Button(bottom_frame, text="ارسال", font=self.font, command=self.send_message)
        send_btn.pack(side=tk.LEFT, padx=5)

        # دکمه خروج
        exit_btn = tk.Button(self.root, text="خروج", font=self.font, command=self.exit_app)
        exit_btn.pack(pady=5)

    def connect_to_server(self):
        try:
            self.socket.connect((self.host, self.port))

            # دریافت نام کاربری
            username_prompt = self.socket.recv(1024).decode()
            self.username = tk.simpledialog.askstring("نام کاربری", username_prompt)
            self.socket.sendall(self.username.encode())

            # شروع دریافت پیام‌ها
            threading.Thread(target=self.receive_messages, daemon=True).start()

            self.root.title(f"پیام‌رسان - {self.username}")
        except Exception as e:
            messagebox.showerror("خطا", f"اتصال ناموفق: {e}")
            self.root.destroy()

    def receive_messages(self):
        while True:
            try:
                message = self.socket.recv(1024).decode()
                if not message:
                    break

                self.display_message(message)
            except:
                break

    def display_message(self, message):
        self.chat_box.config(state='normal')
        self.chat_box.insert(tk.END, message + "\n")
        self.chat_box.config(state='disabled')
        self.chat_box.see(tk.END)

    def send_message(self, event=None):
        message = self.msg_entry.get()
        if message:
            if message.startswith("/"):
                if message == "/exit":
                    self.exit_app()
                    return

            try:
                self.socket.sendall(message.encode())
                self.msg_entry.delete(0, tk.END)
            except:
                messagebox.showerror("خطا", "ارسال ناموفق!")

    def exit_app(self):
        try:
            self.socket.sendall("/exit".encode())
        except:
            pass
        finally:
            self.root.destroy()

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.exit_app)
        self.root.mainloop()


if __name__ == "__main__":
    client = ChatClient()
    client.run()