import tkinter as tk
from tkinter import messagebox

def konversi():
    biner = entry_biner.get()

    # Validasi input (harus 0 dan 1)
    if not all(char in '01' for char in biner):
        messagebox.showerror("Error", "Input harus berupa angka biner (0 dan 1)!")
        return

    # Proses Konversi
    desimal = int(biner, 2)
    heksadesimal = hex(desimal)[2:].upper()

    # Tampilkan hasil
    label_hasil.config(
        text=f"Bilangan Biner       : {biner}\n"
             f"Bilangan Desimal     : {desimal}\n"
             f"Bilangan Heksadesimal: {heksadesimal}",
        fg="white"
    )

# ==================== UI ====================
window = tk.Tk()
window.title("Konversi Biner ke Desimal & Heksadesimal")
window.geometry("500x350")
window.configure(bg="#1E90FF")

# Judul
judul = tk.Label(window, text="PROGRAM KONVERSI BILANGAN",
                 font=("Arial", 18, "bold"), bg="#1E90FF", fg="white")
judul.pack(pady=10)

subjudul = tk.Label(window, text="Biner → Desimal & Heksadesimal",
                    font=("Arial", 14), bg="#1E90FF", fg="white")
subjudul.pack(pady=5)

# Input
tk.Label(window, text="Masukkan Bilangan Biner:",
         font=("Arial", 12), bg="#1E90FF", fg="white").pack()
entry_biner = tk.Entry(window, font=("Arial", 14), justify="center")
entry_biner.pack(pady=10)

# Tombol
btn = tk.Button(window, text="Konversi",
                font=("Arial", 12, "bold"),
                bg="#32CD32", fg="white",
                activebackground="#228B22",
                width=12, command=konversi)
btn.pack(pady=10)

# Hasil
label_hasil = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#1E90FF")
label_hasil.pack(pady=15)

# ==== Tambahan nama kiri bawah ====
label_nama = tk.Label(window, text="ROHANA (41)", font=("Arial", 11, "bold"),
                      bg="#1E90FF", fg="white")
label_nama.place(x=10, y=320)

window.mainloop()
