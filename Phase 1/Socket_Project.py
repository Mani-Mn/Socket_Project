import socket
import threading

def run_server():
    # تنظیمات سرور
    HOST = '127.0.0.1'  # آدرس لوکال
    PORT = 8080  # پورت مورد استفاده

    # ایجاد سوکت
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))  # اتصال به آدرس و پورت
        s.listen()  # گوش دادن به اتصالات
        print(f"سرور در حال اجراست و روی {HOST}:{PORT} منتظر اتصال...")

        conn, addr = s.accept()  # پذیرش اتصال کلاینت
        with conn:
            print('اتصال از:', addr)
            while True:
                data = conn.recv(1024)  # دریافت پیام کلاینت
                if not data:
                    break
                print("پیام دریافتی:", data.decode())

                # ارسال پاسخ به کلاینت
                response = input("پاسخ سرور (برای خروج 'exit' وارد کنید): ")
                if response.lower() == 'exit':
                    break
                conn.sendall(response.encode())


def run_client():
    # تنظیمات سرور
    HOST = '127.0.0.1'  # آدرس سرور
    PORT = 8080  # پورت سرور

    # ایجاد سوکت و اتصال به سرور
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"به سرور {HOST}:{PORT} متصل شدید.")

        while True:
            # ارسال پیام به سرور
            message = input("پیام شما (برای خروج 'exit' وارد کنید): ")
            if message.lower() == 'exit':
                break
            s.sendall(message.encode())

            # دریافت پاسخ از سرور
            data = s.recv(1024)
            print("پاسخ سرور:", data.decode())


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python socket_project.py [server|client]")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "server":
        run_server()
    elif mode == "client":
        run_client()
    else:
        print("Invalid mode. Use 'server' or 'client'")