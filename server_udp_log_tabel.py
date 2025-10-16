import socket
from datetime import datetime

# Membuat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Alamat dan port server
server_address = ('127.0.0.1', 8888)
server_socket.bind(server_address)

print("=== SERVER UDP AKTIF ===")
print("Menunggu pesan dari client...\n")

# Nama file log
log_file = "log_server.txt"

# Header tabel log (ditulis hanya sekali jika file baru)
with open(log_file, "a") as f:
    f.write("=".center(80, "=") + "\n")
    f.write(f"{'WAKTU':<20} | {'IP':<15} | {'PORT':<6} | PESAN\n")
    f.write("-" * 80 + "\n")

# Fungsi mencatat log ke file
def catat_log(client_addr, pesan):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip, port = client_addr
    with open(log_file, "a") as f:
        f.write(f"{waktu:<20} | {ip:<15} | {port:<6} | {pesan}\n")

# Fungsi logika pembalas pesan
def balas_pesan(pesan):
    pesan_lower = pesan.lower()
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if "halo" in pesan_lower or "hai" in pesan_lower:
        return f"Halo juga! Senang menerima pesanmu ({waktu})"
    elif "siapa" in pesan_lower:
        return "Saya adalah server UDP sederhana 😄"
    elif "waktu" in pesan_lower:
        return f"Sekarang waktu server: {waktu}"
    elif "terima kasih" in pesan_lower:
        return "Sama-sama! Semoga harimu menyenangkan 🌞"
    elif "kabar" in pesan_lower:
        return "Saya baik, terima kasih! Kamu gimana?"
    else:
        # Default jika pesan tidak dikenali
        return f"Pesan '{pesan}' diterima oleh server pada {waktu}"

# Loop utama server
while True:
    try:
        data, client_address = server_socket.recvfrom(1024)
        pesan = data.decode()

        print(f"[{client_address}] Pesan: {pesan}")

        # Catat pesan ke file log
        catat_log(client_address, pesan)

        # Proses logika balasan
        balasan = balas_pesan(pesan)

        # Kirim balasan ke client
        server_socket.sendto(balasan.encode(), client_address)

    except KeyboardInterrupt:
        print("\nServer dihentikan secara manual.")
        break
