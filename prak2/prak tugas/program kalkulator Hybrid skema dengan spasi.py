print("=== Kalkulator Hybrid (Dengan Spasi) ===")
ekspresi = input("Input Ekspresi (contoh: 5 - 3 * 4): ")

# Pisahkan berdasarkan spasi
bagian = ekspresi.split()

# Periksa struktur: harus angka-operator-angka
if len(bagian) < 3:
    print("⚠️ Error: Ekspresi terlalu pendek!")
    exit()

# Konversi awal
try:
    total = float(bagian[0])
except:
    print("⚠️ Error: Ekspresi harus diawali angka!")
    exit()

# Tampilkan langkah awal
print("\nHasil Diproses:")
print(f"{bagian[0]} = {total}")

# Proses perhitungan kiri ke kanan
i = 1
while i < len(bagian)-1:
    operator = bagian[i]
    try:
        nilai = float(bagian[i+1])
    except:
        print("⚠️ Error: Setelah operator harus angka!")
        exit()

    if operator == '+':
        new_total = total + nilai
        print(f"{total} + {nilai} = {new_total}")
    elif operator == '-':
        new_total = total - nilai
        print(f"{total} - {nilai} = {new_total}")
    elif operator == '*':
        new_total = total * nilai
        print(f"{total} * {nilai} = {new_total}")
    elif operator == '/':
        if nilai == 0:
            print("⚠️ Error: Pembagian dengan nol tidak boleh!")
            exit()
        new_total = total / nilai
        print(f"{total} / {nilai} = {new_total}")
    else:
        print(f"⚠️ Error: Operator '{operator}' tidak dikenali!")
        exit()

    total = new_total
    i += 2

print("\nOutput >", total)
