import itertools

# Permutasi menyeluruh
def permutasi_menyeluruh(arr):
    return list(itertools.permutations(arr))

# Permutasi sebagian
def permutasi_sebagian(arr, k):
    return list(itertools.permutations(arr, k))

# Permutasi keliling
def permutasi_keliling(arr):
    if len(arr) <= 1:
        return [arr]
    pertama = arr[0]
    sisa = arr[1:]
    hasil = []
    for perm in itertools.permutations(sisa):
        hasil.append([pertama] + list(perm))
    return hasil

# Permutasi berkelompok
def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil

# Menu utama
def main():
    print("=== Program Permutasi Umum ===")
    print("1. Permutasi Menyeluruh")
    print("2. Permutasi Sebagian")
    print("3. Permutasi Keliling")
    print("4. Permutasi Berkelompok")

    pilihan = int(input("Pilih jenis permutasi (1-4): "))

    if pilihan == 1:
        data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
        print("Hasil:", permutasi_menyeluruh(data))

    elif pilihan == 2:
        data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
        k = int(input("Masukkan jumlah elemen yang diambil (k): "))
        print("Hasil:", permutasi_sebagian(data, k))

    elif pilihan == 3:
        data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
        print("Hasil:", permutasi_keliling(data))

    elif pilihan == 4:
        n = int(input("Masukkan jumlah grup: "))
        grup = []
        for i in range(n):
            elemen = input(f"Masukkan elemen grup ke-{i+1} (pisahkan spasi): ").split()
            grup.append(elemen)
        print("Hasil:", permutasi_berkelompok(grup))

    else:
        print("Pilihan tidak valid!")

# Jalankan program
main()
