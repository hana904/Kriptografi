import tkinter as tk
from tkinter import ttk, messagebox

# ===== LATIHAN 1 =====
def latihan1_hitung():
    try:
        a = float(l1_entry1.get())
        b = float(l1_entry2.get())

        hasil_tambah = a + b
        hasil_kurang = a - b
        hasil_kali = a * b
        hasil_bagi = a / b if b != 0 else "Error: Tidak bisa dibagi 0!"

        l1_label_hasil.config(
            text=f"Hasil Penjumlahan: {hasil_tambah}\n"
                 f"Hasil Pengurangan: {hasil_kurang}\n"
                 f"Hasil Perkalian: {hasil_kali}\n"
                 f"Hasil Pembagian: {hasil_bagi}"
        )
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

# ===== LATIHAN 2 =====
def latihan2_hitung():
    try:
        a = float(l2_entry1.get())
        b = float(l2_entry2.get())
        operator = l2_operator.get()

        if operator == '+':
            hasil = a + b
        elif operator == '-':
            hasil = a - b
        elif operator == '*':
            hasil = a * b
        elif operator == '/':
            if b == 0:
                messagebox.showerror("Error", "Pembagian dengan nol tidak diizinkan.")
                return
            hasil = a / b
        else:
            messagebox.showerror("Error", "Operator tidak valid.")
            return

        l2_label_hasil.config(text=f"Hasil: {hasil}")
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

# ===== LATIHAN 3 =====
def hitung_nilai_akhir(sikap, tugas, uts, uas):
    return (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

def konversi_nilai(nilai):
    if 81 <= nilai <= 100:
        return "A", 4
    elif 76 <= nilai <= 80:
        return "B+", 3.5
    elif 71 <= nilai <= 75:
        return "B", 3
    elif 66 <= nilai <= 70:
        return "C+", 2.5
    elif 56 <= nilai <= 65:
        return "C", 2
    elif 46 <= nilai <= 55:
        return "D", 1
    else:
        return "E", 0

def latihan3_hitung():
    try:
        sikap = float(l3_entry_sikap.get())
        tugas = float(l3_entry_tugas.get())
        uts   = float(l3_entry_uts.get())
        uas   = float(l3_entry_uas.get())

        total = hitung_nilai_akhir(sikap, tugas, uts, uas)
        huruf, bobot = konversi_nilai(total)

        hasil = f"Total Nilai: {total:.2f}\nNilai Huruf: {huruf}\nBobot: {bobot}\n"
        hasil += "Keterangan: LULUS" if total >= 56 else "Keterangan: TIDAK LULUS"

        l3_label_hasil.config(text=hasil)
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

# ===== MAIN WINDOW =====
root = tk.Tk()
root.title("Menu Utama Latihan 1 - 2 - 3")
root.geometry("500x400")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# --- Tab Latihan 1 ---
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Latihan 1 (Aritmatika)")

tk.Label(tab1, text="Masukkan angka pertama:").pack()
l1_entry1 = tk.Entry(tab1)
l1_entry1.pack()

tk.Label(tab1, text="Masukkan angka kedua:").pack()
l1_entry2 = tk.Entry(tab1)
l1_entry2.pack()

tk.Button(tab1, text="Hitung Semua Operasi", command=latihan1_hitung, bg="lightblue").pack(pady=10)
l1_label_hasil = tk.Label(tab1, text="Hasil akan muncul di sini", justify="left")
l1_label_hasil.pack()

# --- Tab Latihan 2 ---
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Latihan 2 (Kalkulator)")

tk.Label(tab2, text="Masukkan angka pertama:").pack()
l2_entry1 = tk.Entry(tab2)
l2_entry1.pack()

tk.Label(tab2, text="Masukkan angka kedua:").pack()
l2_entry2 = tk.Entry(tab2)
l2_entry2.pack()

tk.Label(tab2, text="Pilih operator:").pack()
l2_operator = tk.StringVar(value='+')
opsi = ['+', '-', '*', '/']
ttk.OptionMenu(tab2, l2_operator, *opsi).pack()

tk.Button(tab2, text="Hitung", command=latihan2_hitung, bg="lightgreen").pack(pady=10)
l2_label_hasil = tk.Label(tab2, text="Hasil: -", font=("Arial", 12, "bold"))
l2_label_hasil.pack()

# --- Tab Latihan 3 ---
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Latihan 3 (Nilai Akademik)")

tk.Label(tab3, text="Nilai Sikap/Kehadiran (0-100):").pack()
l3_entry_sikap = tk.Entry(tab3)
l3_entry_sikap.pack()

tk.Label(tab3, text="Nilai Tugas (0-100):").pack()
l3_entry_tugas = tk.Entry(tab3)
l3_entry_tugas.pack()

tk.Label(tab3, text="Nilai UTS (0-100):").pack()
l3_entry_uts = tk.Entry(tab3)
l3_entry_uts.pack()

tk.Label(tab3, text="Nilai UAS (0-100):").pack()
l3_entry_uas = tk.Entry(tab3)
l3_entry_uas.pack()

tk.Button(tab3, text="Hitung Nilai Akhir", command=latihan3_hitung, bg="orange").pack(pady=10)
l3_label_hasil = tk.Label(tab3, text="Hasil akan muncul di sini", justify="left")
l3_label_hasil.pack()

root.mainloop()
