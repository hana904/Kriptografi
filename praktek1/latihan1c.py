import tkinter as tk
from tkinter import messagebox

# Fungsi operasi
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Tidak bisa dibagi 0!"

# Fungsi tombol Hitung
def hitung():
    try:
        a = float(entry_angka1.get())
        b = float(entry_angka2.get())

        hasil_tambah = tambah(a, b)
        hasil_kurang = kurang(a, b)
        hasil_kali = kali(a, b)
        hasil_bagi = bagi(a, b)

        hasil_text = (
            f"Hasil Penjumlahan: {hasil_tambah}\n"
            f"Hasil Pengurangan: {hasil_kurang}\n"
            f"Hasil Perkalian: {hasil_kali}\n"
            f"Hasil Pembagian: {hasil_bagi}"
        )

        label_hasil.config(text=hasil_text)
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

# --- GUI ---
root = tk.Tk()
root.title("Latihan 1 - Aritmatika Dasar")
root.geometry("400x300")

# Input angka 1
tk.Label(root, text="Masukkan angka pertama:").pack()
entry_angka1 = tk.Entry(root)
entry_angka1.pack()

# Input angka 2
tk.Label(root, text="Masukkan angka kedua:").pack()
entry_angka2 = tk.Entry(root)
entry_angka2.pack()

# Tombol hitung
btn_hitung = tk.Button(root, text="Hitung Semua Operasi", command=hitung, bg="lightblue")
btn_hitung.pack(pady=10)

# Label hasil
label_hasil = tk.Label(root, text="Hasil akan muncul di sini", font=("Arial", 10), justify="left")
label_hasil.pack(pady=10)

root.mainloop()
        