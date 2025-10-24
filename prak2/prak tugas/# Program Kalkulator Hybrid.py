print("=== Kalkulator Hybrid (Tanpa Spasi) ===")
ekspresi = input("Input Ekspresi (contoh 4+4-3): ")

# Periksa apakah input mengandung spasi
if " " in ekspresi:
    print("⚠️ Error: Input tidak boleh menggunakan spasi!")
    exit()

# Pisahkan angka dan operator
angka = ""
data = []

for char in ekspresi:
    if char.isdigit():
        angka += char
    else:
        if angka == "":
            print("⚠️ Error: Ekspresi tidak valid (operator di awal/tidak ada angka)!")
            exit()
        data.append(angka)
        data.append(char)
        angka = ""

if angka != "":
    data.append(angka)

# Pastikan tidak diakhiri operator
if data[-1] in "+-*/":
    print("⚠️ Error: Ekspresi tidak valid (diakhiri operator)!")
    exit()

# Proses perhitungan
print("\nHasil Diproses:")
total = int(data[0])
print(f"{data[0]} = {total}")  # langkah awal

i = 1
while i < len(data):
    op = data[i]
    next_num = int(data[i+1])

    if op == "+":
        new_total = total + next_num
        print(f"{total} + {next_num} = {new_total}")
    elif op == "-":
        new_total = total - next_num
        print(f"{total} - {next_num} = {new_total}")
    elif op == "*":
        new_total = total * next_num
        print(f"{total} * {next_num} = {new_total}")
    elif op == "/":
        new_total = total / next_num
        print(f"{total} / {next_num} = {new_total}")
    else:
        print("⚠️ Operator tidak dikenal!")
        break

    total = new_total
    i += 2

print("\nOutput >", total)
