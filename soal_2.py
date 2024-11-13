def is_kabisat(tahun):
    # Kondisi pertama: Tahun harus habis dibagi 400
    if tahun % 400 == 0:
        return True
    
    # Kondisi kedua: Tahun harus habis dibagi 4 dan tidak habis dibagi 100
    if tahun % 4 == 0 and tahun % 100 != 0:
        return True
    
    # Jika tidak memenuhi kedua kondisi di atas, maka bukanlah tahun kabisat
    return False

# Contoh penggunaan fungsi is_kabisat()
tahun = int(input("Masukkan tahun: "))
print(f"Tahun {tahun} adalah tahun kabisat? {is_kabisat(tahun)}")