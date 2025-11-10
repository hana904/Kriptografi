import itertools
import tkinter as tk
from tkinter import ttk, messagebox

# ==========================
# FUNGSI PERMUTASI
# ==========================

def permutasi_menyeluruh(arr):
    return list(itertools.permutations(arr))

def permutasi_sebagian(arr, k):
    return list(itertools.permutations(arr, k))

def permutasi_keliling(arr):
    if len(arr) <= 1:
        return [arr]
    else:
        pertama = arr[0]
        sisa_permutasi = permutasi_menyeluruh(arr[1:])
        hasil = []
        for perm in sisa_permutasi:
            hasil.append([pertama] + list(perm))
        return hasil

def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil


# ==========================
# FUNGSI UNTUK MENJALANKAN PERMUTASI
# ==========================

def jalankan_permutasi():
    pilihan = combo_jenis.get()
    data = entry_data.get().strip()

    if not data:
        messagebox.showwarning("Peringatan", "Masukkan data terlebih dahulu!")
        return

    hasil = []
    try:
        if pilihan == "Permutasi Menyeluruh":
            arr = data.split()
            hasil = permutasi_menyeluruh(arr)

        elif pilihan == "Permutasi Sebagian":
            arr = data.split()
            k = int(entry_k.get())
            hasil = permutasi_sebagian(arr, k)

        elif pilihan == "Permutasi Keliling":
            arr = data.split()
            hasil = permutasi_keliling(arr)

        elif pilihan == "Permutasi Berkelompok":
            grup_input = data.split('|')  # tiap grup dipisah tanda |
            grup = [g.split() for g in grup_input]
            hasil = permutasi_berkelompok(grup)

        # tampilkan hasil di textbox
        text_hasil.delete(1.0, tk.END)
        for h in hasil:
            text_hasil.insert(tk.END, f"{h}\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ==========================
# DESAIN ANTARMUKA TKINTER
# ==========================

root = tk.Tk()
root.title("Program Permutasi - Python GUI")
root.geometry("780x560")
root.configure(bg="#495363")

# --------------------------
# Gaya warna & font global
warna_utama = "#1e3a8a"      # biru tua
warna_latar = "#ffffff"
warna_tombol = "#2563eb"     # biru terang
warna_tombol_hover = "#1d4ed8"
warna_teks = "#0f172a"

font_judul = ("Segoe UI", 18, "bold")
font_label = ("Segoe UI", 11)
font_teks = ("Consolas", 10)
# --------------------------

# Judul
label_judul = tk.Label(root, text="✨ PROGRAM PERMUTASI ✨", 
                       font=font_judul, bg="#eaf0f9", fg=warna_utama)
label_judul.pack(pady=15)

# Frame input
frame_input = tk.Frame(root, bg=warna_latar, relief="groove", bd=2)
frame_input.pack(padx=40, pady=10, fill="x")

tk.Label(frame_input, text="Pilih Jenis Permutasi:", font=font_label, bg=warna_latar, fg=warna_teks).grid(row=0, column=0, padx=10, pady=10, sticky="w")
combo_jenis = ttk.Combobox(frame_input, values=["Permutasi Menyeluruh", "Permutasi Sebagian", "Permutasi Keliling", "Permutasi Berkelompok"], width=35)
combo_jenis.grid(row=0, column=1, padx=10, pady=10)
combo_jenis.current(0)

tk.Label(frame_input, text="Masukkan Elemen:", font=font_label, bg=warna_latar, fg=warna_teks).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_data = tk.Entry(frame_input, width=50, font=font_teks)
entry_data.grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame_input, text="Masukkan nilai k (untuk Permutasi Sebagian):", font=font_label, bg=warna_latar, fg=warna_teks).grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_k = tk.Entry(frame_input, width=10, font=font_teks)
entry_k.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Tombol proses
def on_enter(e): btn_proses.config(bg=warna_tombol_hover)
def on_leave(e): btn_proses.config(bg=warna_tombol)

btn_proses = tk.Button(root, text="🔁 Jalankan Permutasi", font=("Segoe UI", 11, "bold"),
                       bg=warna_tombol, fg="white", activebackground=warna_tombol_hover,
                       relief="raised", padx=12, pady=6, command=jalankan_permutasi, cursor="hand2")
btn_proses.pack(pady=15)
btn_proses.bind("<Enter>", on_enter)
btn_proses.bind("<Leave>", on_leave)

# Output area
frame_output = tk.Frame(root, bg="#3d5369", relief="ridge", bd=2)
frame_output.pack(padx=40, pady=10, fill="both", expand=True)

tk.Label(frame_output, text="Hasil Permutasi:", font=("Segoe UI", 11, "bold"), bg="#c5ccae", fg=warna_teks).pack(anchor="w", padx=10, pady=5)
text_hasil = tk.Text(frame_output, height=12, font=font_teks, bg="#f1f5f9", fg="#111827")
text_hasil.pack(padx=10, pady=5, fill="both", expand=True)

# Footer
frame_footer = tk.Frame(root, bg="#90c399")
frame_footer.pack(fill="x", side="bottom", pady=5)

label_kredit = tk.Label(frame_footer, text="ROHANA (41)", font=("Segoe UI", 10, "bold"), 
                        bg="#9fb0c9", fg="#475569", anchor="w")
label_kredit.pack(side="left", padx=15, pady=5)

root.mainloop()
