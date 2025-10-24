import tkinter as tk
from tkinter import messagebox

# Fungsi hitung nilai akhir
def hitung_nilai_akhir(sikap, tugas, uts, uas):
    total = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)
    return total

# Fungsi konversi nilai ke huruf
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

# Fungsi tombol Hitung
def proses_hitung():
    try:
        sikap = float(entry_sikap.get())
        tugas = float(entry_tugas.get())
        uts = float(entry_uts.get())
        uas = float(entry_uas.get())

        total = hitung_nilai_akhir(sikap, tugas, uts, uas)
        huruf, bobot = konversi_nilai(total)

        hasil = f"Total Nilai: {total:.2f}\nNilai Huruf: {huruf}\nBobot: {bobot}\n"

        if total >= 56:
            hasil += "Keterangan: LULUS"
        else:
            hasil += "Keterangan: TIDAK LULUS"

        messagebox.showinfo("Hasil Nilai Akhir", hasil)

    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

# --- GUI ---
root = tk.Tk()
root.title("Hitung Nilai Akhir Akademik")
root.geometry("400x300")

# Label dan entry
tk.Label(root, text="Nilai Sikap/Kehadiran (0-100):").pack()
entry_sikap = tk.Entry(root)
entry_sikap.pack()

tk.Label(root, text="Nilai Tugas (0-100):").pack()
entry_tugas = tk.Entry(root)
entry_tugas.pack()

tk.Label(root, text="Nilai UTS (0-100):").pack()
entry_uts = tk.Entry(root)
entry_uts.pack()

tk.Label(root, text="Nilai UAS (0-100):").pack()
entry_uas = tk.Entry(root)
entry_uas.pack()

# Tombol hitung
btn_hitung = tk.Button(root, text="Hitung Nilai Akhir", command=proses_hitung, bg="lightblue")
btn_hitung.pack(pady=10)

root.mainloop()
