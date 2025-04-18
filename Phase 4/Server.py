import socket
import threading
from datetime import datetime

class ChatServer:
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        self.clients = {}  # {conn: (username, addr)}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setup_server()

    def setup_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"سرور چت در {self.host}:{self.port} فعال است...")
        self.accept_connections()

    def broadcast(self, message, sender_conn=None):
        timestamp = datetime.now().strftime("%H:%M:%S")
        for conn in self.clients.keys():
            if conn != sender_conn:
                try:
                    conn.sendall(f"[{timestamp}] {message}".encode())
                except:
                    self.remove_client(conn)

    def remove_client(self, conn):
        if conn in self.clients:
            username, _ = self.clients[conn]
            del self.clients[conn]
            self.broadcast(f"{username} از چت خارج شد!")
            print(f"کاربر {username} قطع شد")

    def handle_client(self, conn, addr):
        try:
            conn.sendall("نام کاربری خود را وارد کنید: ".encode())
            username = conn.recv(1024).decode().strip()
            self.clients[conn] = (username, addr)
            self.broadcast(f"{username} به چت پیوست!")
            print(f"کاربر جدید: {username} ({addr[0]})")

            while True:
                message = conn.recv(1024).decode()
                if not message:
                    break

                if message.startswith('/pm '):
                    _, target, private_msg = message.split(' ', 2)
                    self.send_private(username, target, private_msg)
                elif message == '/exit':
                    break
                else:
                    self.broadcast(f"{username}: {message}", conn)

        except Exception as e:
            print(f"خطا: {e}")
        finally:
            self.remove_client(conn)
            conn.close()

    def send_private(self, sender, target, message):
        for conn, (username, _) in self.clients.items():
            if username == target:
                timestamp = datetime.now().strftime("%H:%M:%S")
                conn.sendall(f"[PM][{timestamp}] {sender}: {message}".encode())
                return
        print(f"کاربر {target} یافت نشد!")

    def accept_connections(self):
        while True:
            conn, addr = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    server = ChatServer()