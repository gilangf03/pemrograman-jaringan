import socket

# Membuat socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Alamat server (gunakan IP lokal dan port yang sama dengan server)
server_address = ('127.0.0.1', 8888)

print("=== CLIENT UDP ===")
print("Ketik pesan ke server (ketik 'exit' untuk keluar)\n")

while True:
    # Input pesan dari user
    message = input("Pesan: ")

    # Jika user ketik 'exit', keluar dari loop
    if message.lower() == 'exit':
        print("Client keluar.")
        break

    try:
        # Kirim pesan ke server
        client_socket.sendto(message.encode(), server_address)

        # Mencoba menerima balasan dari server
        data, server = client_socket.recvfrom(1024)
        print("Balasan dari server:", data.decode())

    except ConnectionResetError:
        # Menangani jika server belum aktif / koneksi ditolak
        print("⚠️  Tidak dapat terhubung ke server. Pastikan server sudah dijalankan.")
        break

# Tutup socket setelah selesai
client_socket.close()
