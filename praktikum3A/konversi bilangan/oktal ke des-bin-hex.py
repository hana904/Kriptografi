import tkinter as tk
from tkinter import messagebox

def konversi():
    oktal = entry_oktal.get()

    try:
        desimal = int(oktal, 8)
        biner = bin(desimal)[2:]
        hexa = hex(desimal)[2:].upper()

        label_hasil.config(
            text=f"Desimal      : {desimal}\n"
                 f"Biner        : {biner}\n"
                 f"Hexadesimal  : {hexa}",
            fg="white"
        )
    except ValueError:
        messagebox.showerror("Error", "Input hanya boleh angka 0-7 (bilangan Oktal)!")

# ==================== UI ====================
window = tk.Tk()
window.title("Konversi Oktal ke Desimal, Biner, dan Hexadesimal")
window.geometry("550x380")
window.configure(bg="#6A5ACD")  # Ungu gelap

# Judul
judul = tk.Label(window, text="KONVERSI BILANGAN OKTAL",
                 font=("Arial", 20, "bold"),
                 bg="#6A5ACD", fg="white")
judul.pack(pady=10)

subjudul = tk.Label(window, text="Oktal → Desimal | Biner | Hexa",
                    font=("Arial", 14),
                    bg="#6A5ACD", fg="white")
subjudul.pack()

# Label input
tk.Label(window, text="Masukkan Bilangan Oktal:",
         font=("Arial", 12),
         bg="#6A5ACD", fg="white").pack(pady=8)

entry_oktal = tk.Entry(window, font=("Arial", 16), justify="center", width=18)
entry_oktal.pack()

# Tombol
btn = tk.Button(window, text="Konversi",
                font=("Arial", 12, "bold"),
                bg="#32CD32", fg="white",
                width=12, height=1,
                activebackground="#2EB82E",
                command=konversi)
btn.pack(pady=12)

# Kotak hasil
frame_hasil = tk.Frame(window, bg="#4B0082", padx=10, pady=10)
frame_hasil.pack(pady=10)

label_hasil = tk.Label(frame_hasil, text="",
                       font=("Arial", 15, "bold"),
                       bg="#4B0082", fg="white", justify="left")
label_hasil.pack()

# Nama bawah kiri
footer = tk.Label(window, text="ROHANA (41)",
                  font=("Arial", 10, "bold"),
                  bg="#6A5ACD", fg="white", anchor="w")
footer.place(x=10, y=350)

window.mainloop()
