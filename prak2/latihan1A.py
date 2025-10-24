# Program Kalkulator Sederhana
# Menggunakan Operator Aritmatika dan Pengulangan Y/T

while True:
    print("=== Kalkulator Sederhana ===")
    
    # Input nilai
    a = float(input("Masukkan nilai A: "))
    b = float(input("Masukkan nilai B: "))
    
    # Pilih operator
    print("\nPilih operator:")
    print("+  Penjumlahan")
    print("-  Pengurangan")
    print("*  Perkalian")
    print("/  Pembagian")
    print("%  Modulus")
    print("** Pangkat")
    
    op = input("Masukkan operator (+, -, *, /, %, **): ")
    
    # Proses perhitungan
    if op == '+':
        hasil = a + b
    elif op == '-':
        hasil = a - b
    elif op == '*':
        hasil = a * b
    elif op == '/':
        if b != 0:
            hasil = a / b
        else:
            hasil = "Error! Pembagian dengan nol tidak diperbolehkan."
    elif op == '%':
        hasil = a % b
    elif op == '**':
        hasil = a ** b
    else:
        hasil = "Operator tidak valid!"
    
    print(f"\nHasil dari {a} {op} {b} = {hasil}")
    
    # Tanya apakah ingin ulang
    ulang = input("\nApakah ingin menghitung lagi? (Y/T): ").upper()
    if ulang != 'Y':
        print("\nTerima kasih telah menggunakan kalkulator ini 💚")
        break
