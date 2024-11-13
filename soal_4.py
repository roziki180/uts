# Meminta pengguna untuk memasukkan jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang: "))

# Inisialisasi total harga
total_harga = 0

# Menggunakan loop untuk meminta harga setiap barang
for i in range(jumlah_barang):
    harga = float(input(f"Masukkan harga barang ke-{i + 1}: "))
    total_harga += harga  # Menambahkan harga barang ke total

# Menampilkan total harga
print(f"Total harga dari {jumlah_barang} barang adalah: {total_harga}")