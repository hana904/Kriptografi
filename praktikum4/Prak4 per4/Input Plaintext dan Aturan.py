def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext


# --- Input dari user ---
plaintext = input("Masukkan plaintext: ").upper()
aturan_substitusi = {}

print("\nMasukkan aturan substitusi huruf (contoh: A diganti dengan B)")
print("Ketik 'STOP' jika sudah selesai mengisi aturan.\n")

while True:
    huruf_asli = input("Huruf asli (A-Z): ").upper()
    if huruf_asli == 'STOP':
        break
    huruf_ganti = input(f"Ganti '{huruf_asli}' dengan: ").upper()
    aturan_substitusi[huruf_asli] = huruf_ganti

# --- Proses enkripsi ---
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

# --- Hasil output ---
print("\n=== HASIL EKSEKUSI ===")
print(f"Plaintext : {plaintext}")
print(f"Ciphertext: {ciphertext}")
    