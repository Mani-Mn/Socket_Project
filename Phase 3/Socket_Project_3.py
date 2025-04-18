import socket
import threading
from datetime import datetime

# تنظیمات شبکه
HOST = '127.0.0.1'
PORT = 8080

# دیکشنری برای نگهداری کلاینت‌ها {conn: (username, addr)}
clients = {}


def broadcast(message, sender_conn=None):
    """ارسال پیام به همه کلاینت‌ها (به جز فرستنده)"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    formatted_msg = f"[{timestamp}] {message}"

    for conn in clients.keys():
        if conn != sender_conn:
            try:
                conn.sendall(formatted_msg.encode('utf-8'))
            except:
                remove_client(conn)


def remove_client(conn):
    """حذف کلاینت از لیست"""
    if conn in clients:
        username, addr = clients[conn]
        del clients[conn]
        broadcast(f"{username} از چت خارج شد!")
        print(f"[قطع ارتباط] {username} ({addr[0]})")


def handle_client(conn, addr):
    """مدیریت هر کلاینت متصل"""
    try:
        # درخواست نام کاربری
        conn.sendall("لطفاً نام کاربری خود را وارد کنید: ".encode('utf-8'))
        username = conn.recv(1024).decode('utf-8').strip()

        # ثبت کلاینت جدید
        clients[conn] = (username, addr)
        broadcast(f"{username} به چت پیوست!")
        print(f"[اتصال جدید] {username} ({addr[0]})")

        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break

            # پردازش دستورات ویژه
            if data.startswith('/'):
                if data == '/exit':
                    break
                elif data == '/list':
                    online_users = ", ".join([u for u, _ in clients.values()])
                    conn.sendall(f"کاربران آنلاین: {online_users}".encode('utf-8'))
                elif data.startswith('/pm '):
                    parts = data.split(' ', 2)
                    if len(parts) == 3:
                        _, target, msg = parts
                        send_private(username, target, msg)
                continue

            # ارسال پیام عمومی
            broadcast(f"{username}: {data}", conn)

    except Exception as e:
        print(f"[خطا] {addr}: {e}")
    finally:
        remove_client(conn)
        conn.close()


def send_private(sender, target, message):
    """ارسال پیام خصوصی"""
    for conn, (username, _) in clients.items():
        if username == target:
            timestamp = datetime.now().strftime("%H:%M:%S")
            try:
                conn.sendall(f"[پیام خصوصی][{timestamp}] {sender}: {message}".encode('utf-8'))
                return
            except:
                remove_client(conn)
    print(f"کاربر {target} یافت نشد!")


def run_server():
    """راه‌اندازی سرور"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"سرور چت گروهی فعال در {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()


def run_client():
    """راه‌اندازی کلاینت"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))

            # دریافت نام کاربری
            username_prompt = s.recv(1024).decode('utf-8')
            username = input(username_prompt)
            s.sendall(username.encode('utf-8'))

            print("\nدستورات ویژه:\n  /exit - خروج\n  /list - لیست کاربران\n  /pm [کاربر] [پیام] - پیام خصوصی\n")

            # دریافت پیام‌ها در نخ جداگانه
            def receive_messages():
                while True:
                    try:
                        data = s.recv(1024).decode('utf-8')
                        if not data:
                            break
                        print(f"\n{data}")
                    except:
                        break

            threading.Thread(target=receive_messages, daemon=True).start()

            # ارسال پیام‌ها
            while True:
                msg = input()
                if msg.lower() == '/exit':
                    s.sendall('/exit'.encode('utf-8'))
                    break
                s.sendall(msg.encode('utf-8'))

        except ConnectionRefusedError:
            print("سرور یافت نشد! مطمئن شوید سرور اجرا شده است.")
        except Exception as e:
            print(f"خطا: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("طریقه استفاده: python chat_app.py [server|client]")
        sys.exit(1)

    if sys.argv[1] == "server":
        run_server()
    elif sys.argv[1] == "client":
        run_client()
    else:
        print("گزینه نامعتبر! لطفاً 'server' یا 'client' وارد کنید.")