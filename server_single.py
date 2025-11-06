import socket

# Konfigurasi server
HOST = '127.0.0.1'
PORT = 5000

# Membuat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # hanya bisa menangani 1 client
print(f"Server single-thread berjalan di {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Terhubung dengan {addr}")
    data = conn.recv(1024).decode()
    print(f"Pesan diterima: {data}")
    conn.sendall(f"Pesan diterima oleh server: {data}".encode())
    conn.close()
