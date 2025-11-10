import tkinter as tk
from tkinter import messagebox, scrolledtext
import sys

# =========================================================
# LOGIKA VIGENERE CIPHER (PBO)
# =========================================================
class VigenereCipher:
    def __init__(self, key):
        self.key = "".join(filter(str.isalpha, key)).upper()
        if not self.key:
            raise ValueError("Kunci Vigenère tidak boleh kosong.")
        
    def _get_key_stream(self, text):
        text_len = len("".join(filter(str.isalpha, text)))
        key_stream = ""
        key_len = len(self.key)
        for i in range(text_len):
            key_stream += self.key[i % key_len]
        return key_stream

    def encrypt(self, plaintext):
        processed_text = "".join(filter(str.isalpha, plaintext)).upper()
        key_stream = self._get_key_stream(processed_text)
        
        ciphertext = ""
        detail = "=== PROSES ENKRIPSI VIGENERE ===\n"
        key_index = 0

        for char in plaintext.upper():
            if 'A' <= char <= 'Z':
                P = ord(char) - ord('A')
                K = ord(key_stream[key_index]) - ord('A')
                C = (P + K) % 26
                cipher_char = chr(C + ord('A'))
                detail += f"{char}({P}) + {key_stream[key_index]}({K}) = {C} ➜ {cipher_char}\n"
                ciphertext += cipher_char
                key_index += 1
            else:
                ciphertext += char
        return ciphertext, detail

    def decrypt(self, ciphertext):
        processed_text = "".join(filter(str.isalpha, ciphertext)).upper()
        key_stream = self._get_key_stream(processed_text)
        
        plaintext = ""
        detail = "=== PROSES DEKRIPSI VIGENERE ===\n"
        key_index = 0

        for char in ciphertext.upper():
            if 'A' <= char <= 'Z':
                C = ord(char) - ord('A')
                K = ord(key_stream[key_index]) - ord('A')
                P = (C - K) % 26
                plain_char = chr(P + ord('A'))
                detail += f"{char}({C}) - {key_stream[key_index]}({K}) = {P} ➜ {plain_char}\n"
                plaintext += plain_char
                key_index += 1
            else:
                plaintext += char
        return plaintext, detail


# =========================================================
# GUI TKINTER (TAMPILAN MENARIK)
# =========================================================
class VigenereGUI:
    def __init__(self, master):
        self.master = master
        master.title("🔐 VIGENÈRE CIPHER - TUGAS PBO")
        master.geometry("600x580")
        master.configure(bg="#6C63FF")     # Ungu modern

        title = tk.Label(master, text="VIGENÈRE CIPHER ENKRIPSI & DEKRIPSI",
                         font=("Arial", 16, "bold"),
                         bg="#6C63FF", fg="white")
        title.pack(pady=10)

        # FRAME KOTAK PUTIH
        container = tk.Frame(master, bg="white", bd=0, relief=tk.RIDGE)
        container.pack(pady=10, padx=15, fill="both")

        # INPUT TEKS
        tk.Label(container, text="Masukkan Plaintext / Ciphertext:",
                 font=("Arial", 10, "bold"), bg="white").pack(pady=5)
        self.input_text = tk.Text(container, height=3, width=60, font=("Arial", 10))
        self.input_text.pack()

        # INPUT KUNCI
        tk.Label(container, text="Masukkan Kunci (Key):",
                 font=("Arial", 10, "bold"), bg="white").pack(pady=5)
        self.key_entry = tk.Entry(container, width=45, font=("Arial", 11))
        self.key_entry.pack()

        # FRAME TOMIBOL
        btn_frame = tk.Frame(container, bg="white")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="🔒 ENKRIPSI",
                  command=lambda: self.process("encrypt"),
                  bg="#27ae60", fg="white",
                  width=12, font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=8)

        tk.Button(btn_frame, text="🔓 DEKRIPSI",
                  command=lambda: self.process("decrypt"),
                  bg="#2980b9", fg="white",
                  width=12, font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=8)

        tk.Button(btn_frame, text="🧹 CLEAR",
                  command=self.clear_all,
                  bg="#e74c3c", fg="white",
                  width=10, font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=8)

        # OUTPUT HASIL
        tk.Label(container, text="Hasil (Cipher / Plain):",
                 font=("Arial", 10, "bold"), bg="white").pack()
        self.output_text = tk.Text(container, height=2, width=60,
                                   font=("Arial", 11), state=tk.DISABLED)
        self.output_text.pack(pady=5)

        # DETAIL PROSES
        tk.Label(container, text="Detail Proses:",
                 font=("Arial", 10, "bold"), bg="white").pack()
        self.detail_output = scrolledtext.ScrolledText(container, height=8, width=60,
                                                       font=("Consolas", 9),
                                                       state=tk.DISABLED)
        self.detail_output.pack(pady=5)

        # ✅ ROHANA (41) POJOK KIRI BAWAH
        self.footer = tk.Label(master, text="ROHANA (41)",
                               font=("Arial", 10, "bold"),
                               bg="#6C63FF", fg="white")
        self.footer.place(x=10, y=555)


    def set_text(self, widget, content):
        widget.config(state=tk.NORMAL)
        widget.delete("1.0", tk.END)
        widget.insert(tk.END, content)
        widget.config(state=tk.DISABLED)

    def process(self, mode):
        text = self.input_text.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()

        if not text or not key:
            messagebox.showerror("Error", "Teks dan kunci tidak boleh kosong!")
            return

        try:
            cipher = VigenereCipher(key)

            if mode == "encrypt":
                result, detail = cipher.encrypt(text)

            else:
                result, detail = cipher.decrypt(text)

            self.set_text(self.output_text, result)
            self.set_text(self.detail_output, detail)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.key_entry.delete(0, tk.END)
        self.set_text(self.output_text, "")
        self.set_text(self.detail_output, "")


# RUN
if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereGUI(root)
    root.mainloop()
