# ==========================================
# TEORI ELGAMAL - UI MENARIK
# ROHANA 41
# ==========================================

import tkinter as tk
from tkinter import ttk

# --------------------------
# Parameter ElGamal
# --------------------------
p = 29
g = 2
x = 5
k = 7

# --------------------------
# Fungsi Proses
# --------------------------
def proses_elgamal():
    output.config(state="normal")
    output.delete(1.0, tk.END)

    plaintext = entry_plaintext.get().upper()

    # PARAMETER
    output.insert(tk.END, "📌 PARAMETER ELGAMAL\n")
    output.insert(tk.END, f"p = {p}\n")
    output.insert(tk.END, f"g = {g}\n")
    output.insert(tk.END, f"x (private key) = {x}\n")
    output.insert(tk.END, f"k (random) = {k}\n\n")

    # PEMBANGKITAN KUNCI
    output.insert(tk.END, "🔑 PEMBANGKITAN KUNCI\n")
    y = pow(g, x, p)
    output.insert(tk.END, f"y = g^x mod p = {g}^{x} mod {p} = {y}\n")
    output.insert(tk.END, f"Kunci Publik : ({p}, {g}, {y})\n")
    output.insert(tk.END, f"Kunci Privat : {x}\n\n")

    # PLAINTEXT
    output.insert(tk.END, "📝 PLAINTEXT\n")
    output.insert(tk.END, f"{plaintext}\n\n")

    # ASCII
    output.insert(tk.END, "🔢 KONVERSI ASCII\n")
    ascii_vals = []
    for c in plaintext:
        val = ord(c)
        ascii_vals.append(val)
        output.insert(tk.END, f"{c} → {val}\n")

    # ASCII MOD p
    output.insert(tk.END, "\n📦 BLOK PLAINTEXT (m₁, m₂, ...)\n")
    m_vals = []
    for i, a in enumerate(ascii_vals, start=1):
        m = a % p
        m_vals.append(m)
        output.insert(tk.END, f"m{i} = {a} mod {p} = {m}\n")

    # ENKRIPSI
    output.insert(tk.END, "\n🔐 PROSES ENKRIPSI\n")
    a_val = pow(g, k, p)
    yk = pow(y, k, p)

    output.insert(tk.END, f"a = g^k mod p = {a_val}\n")
    output.insert(tk.END, f"y^k mod p = {yk}\n\n")

    for i, m in enumerate(m_vals, start=1):
        b = (m * yk) % p
        output.insert(tk.END, f"b{i} = {m} × {yk} mod {p} = {b}\n")

    # CIPHERTEXT
    output.insert(tk.END, "\n📨 CIPHERTEXT\n")
    for m in m_vals:
        b = (m * yk) % p
        output.insert(tk.END, f"({a_val}, {b}) ")

    output.config(state="disabled")

# --------------------------
# UI SETUP
# --------------------------
root = tk.Tk()
root.title("TEORI ELGAMAL")
root.geometry("900x620")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

# Header
header = tk.Frame(root, bg="#2c3e50", height=70)
header.pack(fill="x")

label_catatan = tk.Label(
    header, text="ROHANA 41",
    bg="#2c3e50", fg="white",
    font=("Arial", 10)
)
label_catatan.place(x=15, y=10)

label_judul = tk.Label(
    header, text="TEORI ELGAMAL",
    bg="#2c3e50", fg="white",
    font=("Arial", 22, "bold")
)
label_judul.pack(pady=15)

# Konten
content = tk.Frame(root, bg="#f4f6f8")
content.pack(fill="both", expand=True, pady=10)

# Input
frame_input = tk.LabelFrame(
    content, text="Input Plaintext",
    bg="#f4f6f8", font=("Arial", 11, "bold")
)
frame_input.pack(fill="x", padx=20, pady=10)

entry_plaintext = ttk.Entry(frame_input, width=40, font=("Arial", 11))
entry_plaintext.pack(side="left", padx=10, pady=10)
entry_plaintext.insert(0, "ROHANALABORA")

btn = ttk.Button(frame_input, text="PROSES ELGAMAL", command=proses_elgamal)
btn.pack(side="left", padx=10)

# Output
frame_output = tk.LabelFrame(
    content, text="Hasil Proses",
    bg="#f4f6f8", font=("Arial", 11, "bold")
)
frame_output.pack(fill="both", expand=True, padx=20, pady=10)

output = tk.Text(
    frame_output,
    font=("Consolas", 10),
    bg="white",
    state="disabled"
)
output.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
