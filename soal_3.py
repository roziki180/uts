# Program menghitung total harga barang

# Meminta jumlah barang dari pengguna
jumlah_barang = int(input("Masukkan jumlah barang: "))

# Inisialisasi total harga
total_harga = 0

# Loop untuk memasukkan harga masing-masing barang
for i in range(jumlah_barang):
    harga = float(input(f"Masukkan harga barang ke-{i+1}: "))
    total_harga += harga  # Tambahkan harga ke total

# Menampilkan total harga
print(f"Total harga dari {jumlah_barang} barang adalah: Rp{total_harga}")


