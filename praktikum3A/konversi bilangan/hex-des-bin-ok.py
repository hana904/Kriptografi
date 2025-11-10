import tkinter as tk
from tkinter import messagebox

def konversi():
    hex_input = entry_hex.get().upper()
    valid_chars = "0123456789ABCDEF"

    # Validasi input
    if not all(char in valid_chars for char in hex_input):
        messagebox.showerror("Error", "Input harus berupa Hexadesimal (0-9 / A-F)!")
        return

    # Proses konversi
    desimal = int(hex_input, 16)
    biner = bin(desimal)[2:]
    oktal = oct(desimal)[2:]

    label_hasil.config(
        text=f"Hexadesimal : {hex_input}\n"
             f"Desimal     : {desimal}\n"
             f"Biner       : {biner}\n"
             f"Oktal       : {oktal}",
        fg="white"
    )

# ==================== UI ====================
window = tk.Tk()
window.title("Konversi Hexadesimal ke Desimal, Biner, dan Oktal")
window.geometry("500x350")
window.configure(bg="#8A2BE2")  # Ungu

judul = tk.Label(window, text="PROGRAM KONVERSI HEXADESIMAL",
                 font=("Arial", 18, "bold"), bg="#8A2BE2", fg="white")
judul.pack(pady=10)

subjudul = tk.Label(window, text="Hex → Desimal | Biner | Oktal",
                    font=("Arial", 14), bg="#8A2BE2", fg="white")
subjudul.pack(pady=5)

tk.Label(window, text="Masukkan Bilangan Hexadesimal:",
         font=("Arial", 12), bg="#8A2BE2", fg="white").pack()

entry_hex = tk.Entry(window, font=("Arial", 14), justify="center")
entry_hex.pack(pady=10)

btn = tk.Button(window, text="Konversi",
                font=("Arial", 12, "bold"),
                bg="#32CD32", fg="white", width=12,
                command=konversi)
btn.pack(pady=10)

label_hasil = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#8A2BE2")
label_hasil.pack(pady=15)

# Tambahan nama kiri bawah
label_nama = tk.Label(window, text="ROHANA (41)", font=("Arial", 11, "bold"),
                      bg="#8A2BE2", fg="white")
label_nama.place(x=10, y=320)

window.mainloop()
