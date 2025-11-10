import itertools
import tkinter as tk
from tkinter import ttk, messagebox

# =====================================
# FUNGSI UTAMA: MENYUSUN BUKU KE RAK
# =====================================
def susun_buku():
    try:
        n = int(entry_buku.get())
        r = int(entry_rak.get())
        if n <= 0 or r <= 0:
            messagebox.showwarning("Peringatan", "Jumlah buku dan rak harus lebih dari 0!")
            return
    except ValueError:
        messagebox.showwarning("Peringatan", "Masukkan angka yang valid!")
        return

    buku = [f"Buku{i+1}" for i in range(n)]
    rak = [f"Rak{j+1}" for j in range(r)]
    
    hasil = list(itertools.product(rak, repeat=n))

    text_hasil.delete(1.0, tk.END)
    text_hasil.insert(tk.END, f"Total cara menyusun {n} buku di {r} rak = {len(hasil)} cara\n\n")

    for i, susunan in enumerate(hasil, start=1):
        pasangan = [f"{buku[j]} → {susunan[j]}" for j in range(n)]
        text_hasil.insert(tk.END, f"{i}. {', '.join(pasangan)}\n")


# =====================================
# DESAIN GUI
# =====================================

root = tk.Tk()
root.title("Program Penyusunan Buku ke Rak")
root.geometry("780x550")
root.configure(bg="#eaf0f9")

# --------------------------
# Gaya global
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
label_judul = tk.Label(root, text="📚 PROGRAM PENYUSUNAN BUKU KE RAK 📚", 
                       font=font_judul, bg="#eaf0f9", fg=warna_utama)
label_judul.pack(pady=15)

# Frame input
frame_input = tk.Frame(root, bg=warna_latar, relief="groove", bd=2)
frame_input.pack(padx=40, pady=10, fill="x")

tk.Label(frame_input, text="Masukkan jumlah buku:", font=font_label, bg=warna_latar, fg=warna_teks).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_buku = tk.Entry(frame_input, width=15, font=font_teks)
entry_buku.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_input, text="Masukkan jumlah rak:", font=font_label, bg=warna_latar, fg=warna_teks).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_rak = tk.Entry(frame_input, width=15, font=font_teks)
entry_rak.grid(row=1, column=1, padx=10, pady=10)

# Tombol Jalankan
def on_enter(e): btn_proses.config(bg=warna_tombol_hover)
def on_leave(e): btn_proses.config(bg=warna_tombol)

btn_proses = tk.Button(root, text="🔁 Jalankan Program", font=("Segoe UI", 11, "bold"),
                       bg=warna_tombol, fg="white", activebackground=warna_tombol_hover,
                       relief="raised", padx=12, pady=6, command=susun_buku, cursor="hand2")
btn_proses.pack(pady=15)
btn_proses.bind("<Enter>", on_enter)
btn_proses.bind("<Leave>", on_leave)

# Output area
frame_output = tk.Frame(root, bg="#f8fafc", relief="ridge", bd=2)
frame_output.pack(padx=40, pady=10, fill="both", expand=True)

tk.Label(frame_output, text="Hasil Penyusunan:", font=("Segoe UI", 11, "bold"), bg="#f8fafc", fg=warna_teks).pack(anchor="w", padx=10, pady=5)
text_hasil = tk.Text(frame_output, height=12, font=font_teks, bg="#f1f5f9", fg="#111827", wrap="word")
text_hasil.pack(padx=10, pady=5, fill="both", expand=True)

# Footer
frame_footer = tk.Frame(root, bg="#eaf0f9")
frame_footer.pack(fill="x", side="bottom")

label_kredit = tk.Label(frame_footer, text="ROHANA (41)", font=("Segoe UI", 10, "bold"), 
                        bg="#eaf0f9", fg="#475569", anchor="w")
label_kredit.pack(side="left", padx=15, pady=8)

root.mainloop()
