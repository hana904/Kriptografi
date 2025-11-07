import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import sys

# =================================================================
# BAGIAN LOGIKA (PBO VigenereCipher)
# =================================================================

class VigenereCipher:
    """Kelas untuk mengimplementasikan Vigenère Cipher dengan PBO."""
    
    def __init__(self, key):
        # Membersihkan kunci dari karakter non-alfabet dan mengubah ke huruf kapital
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
        # Format detail proses agar mudah dibaca di GUI
        detail_proses = "--- PROSES ENKRIPSI VIGENÈRE ---\n"
        key_index = 0

        for char_plaintext in plaintext.upper():
            if 'A' <= char_plaintext <= 'Z':
                P = ord(char_plaintext) - ord('A')
                K = ord(key_stream[key_index]) - ord('A')
                C = (P + K) % 26
                char_ciphertext = chr(C + ord('A'))
                
                # Format detail proses untuk output
                detail_proses += f"{char_plaintext}({P}) + {key_stream[key_index]}({K}) = {C} - {char_ciphertext}\n"
                
                ciphertext += char_ciphertext
                key_index += 1
            else:
                ciphertext += char_plaintext
                
        return ciphertext, detail_proses

    def decrypt(self, ciphertext):
        processed_text = "".join(filter(str.isalpha, ciphertext)).upper()
        key_stream = self._get_key_stream(processed_text)
        
        plaintext = ""
        # Format detail proses agar mudah dibaca di GUI
        detail_proses = "--- PROSES DEKRIPSI VIGENÈRE ---\n"
        key_index = 0

        for char_ciphertext in ciphertext.upper():
            if 'A' <= char_ciphertext <= 'Z':
                C = ord(char_ciphertext) - ord('A')
                K = ord(key_stream[key_index]) - ord('A')
                P = (C - K) % 26
                char_plaintext = chr(P + ord('A'))
                
                # Format detail proses untuk output
                detail_proses += f"{char_ciphertext}({C}) - {key_stream[key_index]}({K}) = {P} - {char_plaintext}\n"
                
                plaintext += char_plaintext
                key_index += 1
            else:
                plaintext += char_ciphertext

        return plaintext, detail_proses

# =================================================================
# BAGIAN ANTARMUKA PENGGUNA GRAFIS (GUI Tkinter)
# =================================================================

class VigenereGUI:
    def __init__(self, master):
        self.master = master
        master.title("🔐 VIGENÈRE CIPHER - TUGAS PBO")
        master.geometry("550x550")
        master.configure(bg='#ecf0f1')
        
        # Style
        font_label = ('Arial', 10, 'bold')
        font_text = ('Arial', 10)
        
        # --- 1. Input Teks ---
        tk.Label(master, text="Plaintext / Ciphertext:", font=font_label, bg='#ecf0f1').pack(pady=5)
        self.input_text = tk.Text(master, height=3, width=60, font=font_text)
        self.input_text.pack()

        # --- 2. Input Kunci ---
        tk.Label(master, text="Key:", font=font_label, bg='#ecf0f1').pack(pady=5)
        self.key_entry = tk.Entry(master, width=50, font=font_text)
        self.key_entry.pack()

        # --- 3. Tombol Aksi ---
        button_frame = tk.Frame(master, bg='#ecf0f1')
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="🔒 Enkripsi", command=lambda: self.process_cipher('encrypt'), 
                  bg='#2ecc71', fg='white', font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="🔓 Dekripsi", command=lambda: self.process_cipher('decrypt'), 
                  bg='#3498db', fg='white', font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="🧹 Clear", command=self.clear_fields, 
                  bg='#e74c3c', fg='white', font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=10)

        # --- 4. Hasil (Ciphertext / Plaintext) ---
        tk.Label(master, text="Hasil (Ciphertext / Plaintext):", font=font_label, bg='#ecf0f1').pack(pady=5)
        self.output_text = tk.Text(master, height=2, width=60, font=font_text, state=tk.DISABLED)
        self.output_text.pack()

        # --- 5. Detail Proses (+80 Poin) ---
        tk.Label(master, text="🔬 Detail Proses:", font=font_label, bg='#ecf0f1').pack(pady=5)
        # Menggunakan ScrolledText untuk output detail proses yang panjang
        self.detail_output = scrolledtext.ScrolledText(master, height=8, width=60, font=('Monospace', 9), state=tk.DISABLED)
        self.detail_output.pack()

    def update_output(self, text_widget, content):
        """Fungsi pembantu untuk memastikan widget Text/ScrolledText diperbarui."""
        text_widget.config(state=tk.NORMAL) 
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, content)
        text_widget.config(state=tk.DISABLED)
        text_widget.see(tk.END) # Menggulir ke bawah, memastikan hasil terlihat

    def process_cipher(self, operation):
        """Fungsi utama yang dipanggil oleh tombol Enkripsi/Dekripsi."""
        # Mengambil input dari baris 1, kolom 0 (1.0) hingga akhir (tk.END), dan menghapus spasi di akhir (strip)
        input_text_val = self.input_text.get(1.0, tk.END).strip()
        key_val = self.key_entry.get().strip()

        if not input_text_val or not key_val:
            messagebox.showerror("Error Input", "Teks dan Kunci harus diisi!")
            return

        try:
            cipher_engine = VigenereCipher(key_val)
            
            if operation == 'encrypt':
                result, details = cipher_engine.encrypt(input_text_val)
                self.update_output(self.output_text, result)
                self.update_output(self.detail_output, details)
                
            elif operation == 'decrypt':
                result, details = cipher_engine.decrypt(input_text_val)
                self.update_output(self.output_text, result)
                self.update_output(self.detail_output, details)

        except ValueError as e:
            # Menangkap error jika kunci kosong
            messagebox.showerror("Error Kunci", str(e))
        except Exception as e:
            # Menangkap error umum (penting untuk debugging)
            messagebox.showerror("Error Program", f"Terjadi kesalahan: {e}\nSilakan cek konsol untuk detail.")
            # Mencetak ke konsol agar Anda bisa melihat traceback lengkap
            print(f"FATAL ERROR: {e}", file=sys.stderr)

    def clear_fields(self):
        """Fungsi untuk membersihkan semua kolom input dan output."""
        self.input_text.delete(1.0, tk.END)
        self.key_entry.delete(0, tk.END)
        self.update_output(self.output_text, "")
        self.update_output(self.detail_output, "")

# --- Jalankan Aplikasi ---
if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereGUI(root)
    root.mainloop()
