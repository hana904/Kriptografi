# latihan2_rsa_gui.py
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
import math

# ---------------- prime list 50..200 ----------------
def sieve_primes(low, high):
    sieve = [True] * (high+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(high**0.5)+1):
        if sieve[i]:
            for j in range(i*i, high+1, i):
                sieve[j] = False
    return [i for i in range(low, high+1) if sieve[i]]

PRIMES = sieve_primes(50, 200)

# ---------------- extended gcd / modinv trace ----------------
def egcd_no_trace(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd_no_trace(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)

def egcd_trace(a, b):
    steps = []
    A, B = a, b
    while B != 0:
        q = A // B
        r = A % B
        steps.append(f"{A} = {q} * {B} + {r}")
        A, B = B, r
    def egcd(a, b):
        if b == 0:
            return (a, 1, 0)
        g, x1, y1 = egcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)
    g, x, y = egcd(a, b)
    return steps, (g, x, y)

def modinv_trace(e, phi):
    steps, _ = egcd_trace(e, phi)
    trace = []
    trace.append("Euclidean steps:")
    for s in steps:
        trace.append("  " + s)
    g, x, y = egcd_no_trace(e, phi)
    if g != 1:
        trace.append(f"No inverse since gcd({e},{phi}) = {g}")
        return None, trace
    # compute extended gcd to get x
    def egcd(a, b):
        if b == 0:
            return (a, 1, 0)
        g, x1, y1 = egcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)
    g, x, y = egcd(e, phi)
    d = x % phi
    trace.append(f"Extended gcd result: g={g}, x={x}, y={y}")
    trace.append(f"Modular inverse d = x mod phi = {x} mod {phi} = {d}")
    return d, trace

# ---------------- modular exponentiation with steps ----------------
def pow_mod_debug(base, exp, mod):
    steps = []
    res = 1
    b = base % mod
    steps.append(f"Base reduced: {base} mod {mod} = {b}")
    e = exp
    i = 0
    while e > 0:
        if e & 1:
            prev = res
            res = (res * b) % mod
            steps.append(f"bit {i}=1 -> res = ({prev} * {b}) % {mod} = {res}")
        else:
            steps.append(f"bit {i}=0 -> res unchanged ({res})")
        e >>= 1
        i += 1
        if e:
            prevb = b
            b = (b * prevb) % mod
            steps.append(f" square -> b = ({prevb} * {prevb}) % {mod} = {b}")
    steps.append(f"Result: {base}^{exp} mod {mod} = {res}")
    return res, steps

# ---------------- GUI class ----------------
class RSA_GUI:
    def __init__(self, root):
        self.root = root
        root.title("Latihan 2 — RSA Random")
        root.geometry("920x700")
        root.configure(bg="#e8eef5")

        # style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Blue.TButton", font=("Arial", 12, "bold"), padding=8,
                        foreground="white", background="#0b6fa4", borderwidth=0)
        style.map("Blue.TButton", background=[("active", "#095a85")])
        style.configure("Green.TButton", font=("Arial", 12, "bold"), padding=8,
                        foreground="white", background="#27ae60", borderwidth=0)
        style.map("Green.TButton", background=[("active", "#1e8449")])

        # header
        header = tk.Frame(root, bg="#0b6fa4", height=60)
        header.pack(fill="x")
        tk.Label(header, text="Latihan 2 — RSA Random (p,q,e)", bg="#0b6fa4",
                 fg="white", font=("Arial", 18, "bold")).pack(pady=12)

        # top controls
        top = tk.Frame(root, bg="#e8eef5")
        top.pack(fill="x", padx=10, pady=10)

        ttk.Button(top, text="Generate p, q, e", style="Blue.TButton",
                   command=self.generate).pack(side="left", padx=6)
        ttk.Button(top, text="Reset", style="Green.TButton",
                   command=self.reset).pack(side="left", padx=6)

        # use tk.Label (so background consistent)
        tk.Label(top, text="Plaintext:", bg="#e8eef5",
                 font=("Arial", 12, "bold")).pack(side="left", padx=8)
        self.entry_plain = ttk.Entry(top, width=45)
        self.entry_plain.pack(side="left", padx=6)

        ttk.Button(top, text="Encrypt", style="Blue.TButton",
                   command=self.encrypt).pack(side="left", padx=6)
        ttk.Button(top, text="Decrypt", style="Green.TButton",
                   command=self.decrypt).pack(side="left", padx=6)

        # info labels (use tk.Label so we can set bg)
        info = tk.Frame(root, bg="#e8eef5")
        info.pack(fill="x", padx=10, pady=6)
        self.lbl_pq = tk.Label(info, text="p=?, q=?, phi=?, n=?", bg="#e8eef5",
                               font=("Arial", 12, "bold"))
        self.lbl_pq.pack(anchor="w")
        self.lbl_keys = tk.Label(info, text="Public=?, Private=?", bg="#e8eef5",
                                 font=("Arial", 12, "bold"))
        self.lbl_keys.pack(anchor="w")

        # debug text
        self.debug = scrolledtext.ScrolledText(root, font=("Consolas", 11), bg="white", fg="#2c3e50")
        self.debug.pack(fill="both", expand=True, padx=10, pady=10)

        # footer center
        footer = tk.Frame(root, bg="#0b6fa4", height=36)
        footer.pack(fill="x")
        tk.Label(footer, text="ROHANA41", bg="#0b6fa4", fg="white",
                 font=("Arial", 12, "bold")).pack(pady=6)

        # initialize
        self.p = self.q = self.e = self.n = self.phi = self.d = None
        self.last_cipher = None

    def log(self, *args):
        self.debug.insert(tk.END, " ".join(str(a) for a in args) + "\n")
        self.debug.see(tk.END)

    def generate(self):
        self.debug.delete("1.0", tk.END)
        self.p = random.choice(PRIMES)
        self.q = random.choice(PRIMES)
        while self.q == self.p:
            self.q = random.choice(PRIMES)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.log(f"Selected p={self.p}, q={self.q}")
        self.log(f"n = {self.n}")
        self.log(f"phi = {self.phi}")

        # choose e
        cand = list(range(3, self.phi))
        random.shuffle(cand)
        self.e = next((x for x in cand if math.gcd(x, self.phi) == 1), None)
        self.log(f"Chosen e = {self.e}  (gcd={math.gcd(self.e, self.phi)})")

        d, trace = modinv_trace(self.e, self.phi)
        if d is None:
            self.log("ERROR: cannot compute d")
            self.d = None
        else:
            self.d = d
            for t in trace:
                self.log(t)
            self.log(f"Final d = {self.d}")

        self.lbl_pq.config(text=f"p={self.p}, q={self.q}, phi={self.phi}, n={self.n}")
        self.lbl_keys.config(text=f"Public (e,n)=({self.e},{self.n})   Private (d,n)=({self.d},{self.n})")
        self.last_cipher = None

    def reset(self):
        self.debug.delete("1.0", tk.END)
        self.entry_plain.delete(0, tk.END)
        self.lbl_pq.config(text="p=?, q=?, phi=?, n=?")
        self.lbl_keys.config(text="Public=?, Private=?")
        self.p = self.q = self.e = self.n = self.phi = self.d = None
        self.last_cipher = None

    def encrypt(self):
        if not (self.e and self.d):
            messagebox.showwarning("Warning", "Generate kunci terlebih dulu.")
            return
        plaintext = self.entry_plain.get()
        if plaintext == "":
            messagebox.showwarning("Warning", "Masukkan plaintext.")
            return
        self.log("\n=== ENKRIPSI ===")
        self.log("Plaintext:", plaintext)
        ciphertexts = []
        for ch in plaintext:
            M = ord(ch)
            self.log(f"\nChar '{ch}' -> ASCII {M}")
            C, steps = pow_mod_debug(M, self.e, self.n)
            for s in steps:
                self.log("  " + s)
            self.log(f" => Cipher = {C}")
            ciphertexts.append(C)
        self.last_cipher = ciphertexts
        self.log("\nCipher array: " + str(ciphertexts))

    def decrypt(self):
        if not self.last_cipher:
            messagebox.showwarning("Warning", "Belum ada ciphertext.")
            return
        self.log("\n=== DEKRIPSI ===")
        recovered = []
        for C in self.last_cipher:
            self.log(f"\nCipher {C}:")
            M, steps = pow_mod_debug(C, self.d, self.n)
            for s in steps:
                self.log("  " + s)
            ch = chr(M)
            self.log(f" => ASCII={M} -> char='{ch}'")
            recovered.append(ch)
        self.log("\nRecovered: " + "".join(recovered))

# ---------------- main ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = RSA_GUI(root)
    root.mainloop()
