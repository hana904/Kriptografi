# Program Penjumlahan dengan Pengulangan (Soal 1)

ulang = "Y"

while ulang.upper() == "Y":
    a = int(input("Masukkan nilai a: "))
    b = int(input("Masukkan nilai b: "))
    c = a + b
    print("Hasil dari", a, "+", b, "=", c)
    
    ulang = input("Apakah ingin menghitung lagi? (Y/T): ")

print("Program selesai.")
