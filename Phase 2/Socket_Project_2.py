import socket
import threading
import sys

# تنظیمات شبکه
HOST = '127.0.0.1'
PORT = 8080

# لیست کلاینت‌های متصل
clients = []


def handle_client(conn, addr):
    """تابع مدیریت هر کلاینت متصل"""
    print(f"[اتصال جدید] {addr}")
    clients.append(conn)

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            # نمایش پیام به همه کلاینت‌ها (به جز خود فرستنده)
            message = f"{addr}: {data.decode()}"
            print(message)

            # ارسال به همه کلاینت‌ها
            for client in clients:
                if client != conn:
                    client.sendall(message.encode())

    except Exception as e:
        print(f"[خطا برای {addr}]: {e}")
    finally:
        clients.remove(conn)
        conn.close()
        print(f"[قطع ارتباط] {addr}")


def run_server():
    """تابع راه‌اندازی سرور"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"سرور چندنخی فعال روی {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()


def run_client():
    """تابع راه‌اندازی کلاینت"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"به سرور {HOST}:{PORT} متصل شدید.")

        # دریافت پیام‌ها در یک نخ جداگانه
        def receive_messages():
            while True:
                try:
                    data = s.recv(1024)
                    if not data:
                        break
                    print(f"\nپیام جدید: {data.decode()}")
                except:
                    break

        threading.Thread(target=receive_messages, daemon=True).start()

        while True:
            message = input("پیام شما (exit برای خروج): ")
            if message.lower() == 'exit':
                break
            s.sendall(message.encode())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Socket_Project.py [server|client]")
        sys.exit(1)

    if sys.argv[1] == "server":
        run_server()
    elif sys.argv[1] == "client":
        run_client()
    else:
        print("گزینه نامعتبر!")