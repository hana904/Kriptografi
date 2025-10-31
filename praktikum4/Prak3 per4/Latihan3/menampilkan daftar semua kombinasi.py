import itertools

# Fungsi faktorial
def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

# Fungsi kombinasi (menghitung nilai C(n, r))
def kombinasi(n, r):
    if r > n:
        return 0
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

# Program utama
print("=== Program Kombinasi (C(n, r)) ===")
n = int(input("Masukkan jumlah total objek (n): "))
r = int(input("Masukkan jumlah objek yang dipilih (r): "))

# Membuat daftar huruf sebagai inisial (A, B, C, D, ...)
huruf = [chr(65 + i) for i in range(n)]

# Hitung jumlah kombinasi
jumlah = kombinasi(n, r)

# Buat daftar kombinasi aktual menggunakan itertools
daftar_kombinasi = list(itertools.combinations(huruf, r))

# Tampilkan hasil
print(f"\nJumlah kombinasi C({n}, {r}) = {jumlah}")
print(f"Objek yang digunakan: {huruf}\n")

print("Daftar kombinasi yang mungkin:")
for i, combo in enumerate(daftar_kombinasi, start=1):
    print(f"{i}. {combo}")

