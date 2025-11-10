import itertools
import tkinter as tk
from tkinter import messagebox

# Fungsi faktorial
def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

# Fungsi kombinasi
def kombinasi(n, r):
    if r > n:
        return 0
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

# Tombol hitung
def hitung():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())

        if n < 0 or r < 0:
            messagebox.showerror("Error", "n dan r harus bilangan positif!")
            return

        huruf = [chr(65 + i) for i in range(n)]

        jumlah = kombinasi(n, r)
        daftar_kombinasi = list(itertools.combinations(huruf, r))

        listbox.delete(0, tk.END)

        label_hasil.config(
            text=f"Jumlah Kombinasi C({n}, {r}) = {jumlah}\nObjek: {huruf}",
            fg="#2c3e50"
        )

        for i, combo in enumerate(daftar_kombinasi, start=1):
            listbox.insert(tk.END, f"{i}. {combo}")

    except ValueError:
        messagebox.showerror("Error", "Input n dan r wajib angka!")


# ==================== UI ====================

window = tk.Tk()
window.title("Program Kombinasi C(n, r)")
window.geometry("600x600")

# Background warna gradien
bg = tk.Canvas(window, width=600, height=600)
bg.pack(fill="both", expand=True)
bg.create_rectangle(0, 0, 600, 600, fill="#74b9ff")
bg.create_rectangle(0, 300, 600, 600, fill="#0984e3")

# Frame putih elegan
frame = tk.Frame(window, bg="white", bd=0, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=520)

judul = tk.Label(frame, text="PROGRAM KOMBINASI\nC(n, r)",
                 font=("Arial", 18, "bold"), bg="white", fg="#2d3436")
judul.pack(pady=10)

# Input n
tk.Label(frame, text="Masukkan n (Total Objek):", font=("Arial", 12, "bold"),
         bg="white", fg="#2d3436").pack()
entry_n = tk.Entry(frame, font=("Arial", 13), justify="center", bd=2, relief="solid")
entry_n.pack(pady=5)

# Input r
tk.Label(frame, text="Masukkan r (Dipilih):", font=("Arial", 12, "bold"),
         bg="white", fg="#2d3436").pack()
entry_r = tk.Entry(frame, font=("Arial", 13), justify="center", bd=2, relief="solid")
entry_r.pack(pady=5)

# Tombol
btn = tk.Button(frame, text="HITUNG", font=("Arial", 12, "bold"),
                bg="#00b894", fg="white", activebackground="#00916E",
                width=15, command=hitung)
btn.pack(pady=15)

# Hasil jumlah
label_hasil = tk.Label(frame, text="", font=("Arial", 11, "bold"),
                       bg="white", fg="#2c3e50")
label_hasil.pack(pady=5)

# Listbox kombinasi
listbox = tk.Listbox(frame, width=45, height=16, font=("Courier", 10),
                     bg="#dfe6e9", fg="#2d3436", bd=3, relief="sunken")
listbox.pack(pady=10)

# Footer ROHANA(41)
footer = tk.Label(window, text="ROHANA (41)",
                  font=("Arial", 11, "bold"), fg="white", bg="#0984e3")
footer.place(x=10, y=570)

window.mainloop()
