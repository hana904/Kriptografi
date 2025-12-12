# latihan1_rsa_gui.py
# UI Tkinter untuk Latihan 1 RSA (p=17, q=11, e=7)
# Menampilkan langkah-langkah lengkap sesuai modul + catatan "ROHANA41" di bawah

import tkinter as tk
from tkinter import ttk, scrolledtext
import math

# ------------------ Helper math functions ------------------

def egcd(a, b):
    """Extended gcd returning (g, x, y) dengan ax + by = g"""
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)

def pow_mod_steps(base, exp, mod):
    """
    Hitung base^exp mod mod dengan trace langkah-langkah
    menggunakan binary exponentiation (square-and-multiply).
    Mengembalikan (result, list_of_steps).
    """
    steps = []
    value = 1
    b = base % mod
    e = exp
    steps.append(f"Awal: base={base} mod {mod} => b={b}, exp={exp}")
    bit_index = 0
    while e > 0:
        if e & 1:
            prev = value
            value = (value * b) % mod
            steps.append(f"bit {bit_index}=1 -> value = ({prev} * {b}) % {mod} = {value}")
        else:
            steps.append(f"bit {bit_index}=0 -> skip multiply (value tetap {value})")
        e >>= 1
        bit_index += 1
        if e:  # compute next square (b = b^2 mod)
            prevb = b
            b = (b * prevb) % mod
            steps.append(f" square -> b = ({prevb} * {prevb}) % {mod} = {b}")
    steps.append(f"Hasil akhir: {base}^{exp} mod {mod} = {value}")
    return value, steps

# ------------------ RSA steps (fixed p,q,e) ------------------

def compute_and_show(log_widget):
    """Lakukan semua perhitungan dan tampilkan ke log_widget (scrolledtext)."""
    # Clear
    log_widget.delete("1.0", tk.END)

    # Parameters fixed
    p = 17
    q = 11
    e = 7

    def log(*args):
        text = " ".join(str(a) for a in args)
        log_widget.insert(tk.END, text + "\n")
        log_widget.see(tk.END)

    log("=== Latihan 1: RSA dengan p=17, q=11, e=7 ===\n")
    log("1) Pilih p =", p, "q =", q)
    n = p * q
    log("2) Hitung n = p * q =", p, "*", q, "=", n)
    phi = (p - 1) * (q - 1)
    log("3) Hitung phi(n) = (p-1)*(q-1) =", (p - 1), "*", (q - 1), "=", phi)
    log(f"4) Pilih e = {e}, cek: 1 < e < phi -> 1 < {e} < {phi} -> valid?")
    log("   Cek GCD(e, phi) dengan langkah Euclidean:")

    # Euclidean steps to show gcd
    a, b = phi, e
    log(f"   {a} ÷ {b}")
    stepnum = 0
    while b != 0:
        q_div = a // b
        r = a % b
        log(f"   Step {stepnum}: {a} = {q_div} * {b} + {r}")
        a, b = b, r
        stepnum += 1
    log(f"   Sisa terakhir = {a} -> GCD = {a} (harus 1). GCD({e},{phi}) = {a}")
    log("\n=> e memenuhi syarat (GCD=1). Kunci publik = (e, n) = ({}, {})".format(e, n))

    # Cara 1: Diophantine sederhana (coba k=1 sesuai modul)
    log("\n--- Menentukan d (Cara 1: Diophantine sederhana, coba k=1 seperti modul) ---")
    log("Kita ingin {}*d ≡ 1 (mod {})  -> {}*d - {}*k = 1".format(e, phi, e, phi))
    k = 1
    numerator = 1 + phi * k
    log(f"Coba k = {k} -> {e}*d = 1 + {phi}*{k} = {numerator}")
    if numerator % e == 0:
        d = numerator // e
        log(f"-> d = {numerator} / {e} = {d}")
    else:
        log(f"-> {numerator} tidak habis dibagi {e}, tidak menghasilkan integer.")

    # Cara 2: Extended Euclidean & Back-substitution
    log("\n--- Menentukan d (Cara 2: Euclidean + Back-substitution / modular inverse) ---")
    g, x, y = egcd(e, phi)
    log(f"EGCD({e},{phi}) => g={g}, x={x}, y={y}  -> berarti {x}*{e} + {y}*{phi} = {g}")
    if g != 1:
        log("Tidak ada invers modular (g != 1).")
        d_modinv = None
    else:
        d_modinv = x % phi
        log(f"Invers modular d = x mod phi = {x} mod {phi} = {d_modinv}")
        log(f"Jadi d = {d_modinv}")

    # sanity check
    if d_modinv is not None and 'd' in locals() and d_modinv != d:
        log("(Catatan: d dari cara 1 dan cara 2 berbeda — periksa. Seharusnya sama.)")

    log("\nKunci publik: (e, n) = ({}, {})".format(e, n))
    log("Kunci privat: (d, n) = ({}, {})\n".format(d, n))

    # ------------------ PLAINTEXT DIGANTI DI SINI ------------------
    plaintext = "ROHANALABORA"
    # ---------------------------------------------------------------

    log("=== Enkripsi pesan '{}' dengan formula C = M^e mod n ===".format(plaintext))
    ciphertexts = []
    for ch in plaintext:
        M = ord(ch)
        log(f"\nPlaintext '{ch}' -> ASCII = {M}")
        C, steps = pow_mod_steps(M, e, n)
        for s in steps:
            log("   " + s)
        log(f"  >> Ciphertext untuk '{ch}' = {C}")
        ciphertexts.append(C)

    log("\nCiphertext (deret nilai): " + str(ciphertexts))

    log("\n=== Dekripsi pesan dengan M = C^d mod n ===")
    recovered = []
    for i, C in enumerate(ciphertexts):
        ch = plaintext[i]
        log(f"\nCipher {C} (asal '{ch}') -> dekripsi:")
        M_rec, steps = pow_mod_steps(C, d, n)
        for s in steps:
            log("   " + s)
        try:
            char_rec = chr(M_rec)
        except Exception:
            char_rec = f"<non-ASCII:{M_rec}>"
        log(f"  >> M_recovered = {M_rec} -> char = {char_rec}")
        recovered.append(char_rec)

    recovered_text = "".join(recovered)
    log("\nPesan hasil dekripsi: " + recovered_text)
    log("\n=== Latihan 1 selesai ===\n")

# ------------------ Tkinter UI ------------------

def make_ui():
    root = tk.Tk()
    root.title("Latihan 1 RSA - UI (p=17,q=11,e=7)")
    root.geometry("900x700")
    root.configure(bg="#e8eef5")

    # ------------ Style Tombol (modern) ------------
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Tombol.TButton",
                    font=("Arial", 12, "bold"),
                    padding=10,
                    foreground="white",
                    background="#0b6fa4",
                    borderwidth=0)
    style.map("Tombol.TButton",
              background=[("active", "#095a85")])

    style.configure("Copy.TButton",
                    font=("Arial", 12, "bold"),
                    padding=10,
                    foreground="white",
                    background="#27ae60",
                    borderwidth=0)
    style.map("Copy.TButton",
              background=[("active", "#1e8449")])

    # ------------ Header ------------
    header = tk.Frame(root, bg="#0b6fa4", height=60)
    header.pack(fill="x")
    lbl_title = tk.Label(header, text="Latihan 1 — RSA (p=17, q=11, e=7)", bg="#0b6fa4",
                         fg="white", font=("Arial", 18, "bold"), pady=12)
    lbl_title.pack()

    # ------------ Tombol Utama ------------
    top_frame = tk.Frame(root, bg="#e8eef5")
    top_frame.pack(fill="x", padx=10, pady=15)

    btn_run = ttk.Button(top_frame,
                         text="▶ Jalankan Perhitungan Lengkap",
                         style="Tombol.TButton",
                         command=lambda: compute_and_show(txt_log))
    btn_run.pack(side="left", padx=10)

    def copy_log():
        content = txt_log.get("1.0", tk.END)
        root.clipboard_clear()
        root.clipboard_append(content)

    btn_copy = ttk.Button(top_frame,
                          text="📋 Copy Log",
                          style="Copy.TButton",
                          command=copy_log)
    btn_copy.pack(side="left", padx=10)

    # ------------ Area Log ------------
    txt_log = scrolledtext.ScrolledText(root, wrap=tk.WORD,
                                        font=("Consolas", 11),
                                        bg="white", fg="#2c3e50")
    txt_log.pack(fill="both", expand=True, padx=10, pady=10)

    # ------------ Footer (nama di tengah) ------------
    footer = tk.Frame(root, bg="#0b6fa4", height=30)
    footer.pack(fill="x")

    lbl_footer = tk.Label(footer, text="ROHANA41", bg="#0b6fa4", fg="white",
                          font=("Arial", 12, "bold"))
    lbl_footer.pack(pady=4)

    # ------------ Pesan Awal ------------
    txt_log.insert(tk.END, "▶ Tekan tombol di atas untuk menjalankan semua langkah perhitungan RSA.\n")
    txt_log.insert(tk.END, "Hasil akan tampil lengkap sesuai modul (Euclidean, Diophantine, enkripsi, dekripsi).\n\n")

    root.mainloop()


if __name__ == "__main__":
    make_ui()
