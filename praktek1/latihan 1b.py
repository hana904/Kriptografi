import tkinter as tk
from tkinter import messagebox

def hitung():
    try:
        angka1 = float(entry_angka1.get())
        angka2 = float(entry_angka2.get())
        operator = operator_var.get()

        if operator == '+':
            hasil = angka1 + angka2
        elif operator == '-':
            hasil = angka1 - angka2
        elif operator == '*':
            hasil = angka1 * angka2
        elif operator == '/':
            if angka2 == 0:
                messagebox.showerror("Error", "Pembagian dengan nol tidak diizinkan.")
                return
            hasil = angka1 / angka2
        else:
            messagebox.showerror("Error", "Operator tidak valid.")
            return

        label_hasil.config(text=f"Hasil: {hasil}")
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

# --- GUI ---
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("350x250")

# Input angka 1
tk.Label(root, text="Masukkan angka pertama:").pack()
entry_angka1 = tk.Entry(root)
entry_angka1.pack()

# Input angka 2
tk.Label(root, text="Masukkan angka kedua:").pack()
entry_angka2 = tk.Entry(root)
entry_angka2.pack()

# Pilih operator
tk.Label(root, text="Pilih operator:").pack()
operator_var = tk.StringVar(value='+')
opsi = ['+', '-', '*', '/']
dropdown = tk.OptionMenu(root, operator_var, *opsi)
dropdown.pack()

# Tombol hitung
btn_hitung = tk.Button(root, text="Hitung", command=hitung, bg="lightgreen")
btn_hitung.pack(pady=10)

# Label hasil
label_hasil = tk.Label(root, text="Hasil: -", font=("Arial", 12, "bold"))
label_hasil.pack()

root.mainloop()
