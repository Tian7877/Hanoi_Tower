def hanoi_multi(n, start, destination, towers):
    """Menyelesaikan Tower of Hanoi dengan 3 menara secara rekursif."""
    global total_moves
    if n == 1:
        print(f"Pindahkan disk {n} dari Menara {start} ke Menara {destination}")
        total_moves += 1
        return
    # Menentukan menara bantu yang tidak digunakan oleh start dan destination
    aux = [tower for tower in towers if tower != start and tower != destination][0]
    hanoi_multi(n - 1, start, aux, towers)  # Pindahkan disk ke menara bantu
    print(f"Pindahkan disk {n} dari Menara {start} ke Menara {destination}")
    total_moves += 1
    hanoi_multi(n - 1, aux, destination, towers)  # Pindahkan disk dari menara bantu ke tujuan

# Inisialisasi
total_moves = 0
n = int(input("Masukkan N : "))  # Jumlah disk
tower_names = ['A', 'B', 'C', 'D']  # Menara yang tersedia
start = tower_names[0]  # Menara asal
destination = tower_names[3]  # Menara tujuan

hanoi_multi(n, start, destination, tower_names)
print(f"Total pergerakan disk: {total_moves}")


#Ngecek pake metode hanoi biasa dengan metode hanoi yang frame_stewarts