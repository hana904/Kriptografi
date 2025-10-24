# Program Kalkulator Sederhana (Soal 2)

a = float(input("Masukkan nilai A: "))
b = float(input("Masukkan nilai B: "))

print("\nPilih operator:")
print("+  Penjumlahan")
print("-  Pengurangan")
print("*  Perkalian")
print("/  Pembagian")
print("%  Modulus")
print("** Pangkat")

op = input("Masukkan operator (+, -, *, /, %, **): ")

if op == '+':
    hasil = a + b
elif op == '-':
    hasil = a - b
elif op == '*':
    hasil = a * b
elif op == '/':
    hasil = a / b
elif op == '%':
    hasil = a % b
elif op == '**':
    hasil = a ** b
else:
    hasil = "Operator tidak valid!"

print(f"\nHasil dari {a} {op} {b} = {hasil}")
