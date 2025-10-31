# Program Kriptografi Klasik: Substitusi Cipher + Transposisi Cipher
# Versi Latihan Rohana

# Fungsi Substitusi Cipher (Caesar Cipher geser 3)
def substitusi_cipher(plaintext):
    hasil = ""
    print("\nHasil Substitusi (+3):\n")
    print("Huruf Asli | +3 | Hasil")
    print("------------------------")
    for char in plaintext:
        if char.isalpha():
            kode = ord(char.upper())
            kode_baru = ((kode - 65 + 3) % 26) + 65
            hasil_huruf = chr(kode_baru)
            print(f"{char.upper()} | +3 | {hasil_huruf}")
            hasil += hasil_huruf
        else:
            print(f"{char} |    | {char}")
            hasil += char
    return hasil

# Fungsi Transposisi Cipher (4 blok)
def transposisi_cipher(plaintext):
    while len(plaintext) % 4 != 0:  # agar bisa dibagi rata
        plaintext += " "
    
    part_length = len(plaintext) // 4
    parts = [plaintext[i:i + part_length] for i in range(0, len(plaintext), part_length)]

    print("\nProses Transposisi:")
    for i, part in enumerate(parts, start=1):
        print(f"Bagian {i}: {part}")

    ciphertext = ""
    for col in range(part_length):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]

    return ciphertext.strip()

# ====== Eksekusi Utama ======
plaintext = input("Masukkan plaintext: ").upper()
print(f"\nPlaintext: {plaintext}")

# Tahap 1: Substitusi
substitusi = substitusi_cipher(plaintext)
print(f"\nHasil Substitusi Akhir: {substitusi}")

# Tahap 2: Transposisi
transposisi = transposisi_cipher(substitusi)

# Hasil Akhir
print("\n==============================")
print(f"Plaintext               : {plaintext}")
print(f"Substitusi Cipher (+3)  : {substitusi}")
print(f"Transposisi Cipher (4 blok) : {transposisi}")
print("==============================")
