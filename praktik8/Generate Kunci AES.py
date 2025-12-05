import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# ================= SBOX =================
SBOX = [
0x63,0x7C,0x77,0x7B,0xF2,0x6B,0x6F,0xC5,0x30,0x01,0x67,0x2B,0xFE,0xD7,0xAB,0x76,
0xCA,0x82,0xC9,0x7D,0xFA,0x59,0x47,0xF0,0xAD,0xD4,0xA2,0xAF,0x9C,0xA4,0x72,0xC0,
0xB7,0xFD,0x93,0x26,0x36,0x3F,0xF7,0xCC,0x34,0xA5,0xE5,0xF1,0x71,0xD8,0x31,0x15,
0x04,0xC7,0x23,0xC3,0x18,0x96,0x05,0x9A,0x07,0x12,0x80,0xE2,0xEB,0x27,0xB2,0x75,
0x09,0x83,0x2C,0x1A,0x1B,0x6E,0x5A,0xA0,0x52,0x3B,0xD6,0xB3,0x29,0xE3,0x2F,0x84,
0x53,0xD1,0x00,0xED,0x20,0xFC,0xB1,0x5B,0x6A,0xCB,0xBE,0x39,0x4A,0x4C,0x58,0xCF,
0xD0,0xEF,0xAA,0xFB,0x43,0x4D,0x33,0x85,0x45,0xF9,0x02,0x7F,0x50,0x3C,0x9F,0xA8,
0x51,0xA3,0x40,0x8F,0x92,0x9D,0x38,0xF5,0xBC,0xB6,0xDA,0x21,0x10,0xFF,0xF3,0xD2,
0xCD,0x0C,0x13,0xEC,0x5F,0x97,0x44,0x17,0xC4,0xA7,0x7E,0x3D,0x64,0x5D,0x19,0x73,
0x60,0x81,0x4F,0xDC,0x22,0x2A,0x90,0x88,0x46,0xEE,0xB8,0x14,0xDE,0x5E,0x0B,0xDB,
0xE0,0x32,0x3A,0x0A,0x49,0x06,0x24,0x5C,0xC2,0xD3,0xAC,0x62,0x91,0x95,0xE4,0x79,
0xE7,0xC8,0x37,0x6D,0x8D,0xD5,0x4E,0xA9,0x6C,0x56,0xF4,0xEA,0x65,0x7A,0xAE,0x08,
0xBA,0x78,0x25,0x2E,0x1C,0xA6,0xB4,0xC6,0xE8,0xDD,0x74,0x1F,0x4B,0xBD,0x8B,0x8A,
0x70,0x3E,0xB5,0x66,0x48,0x03,0xF6,0x0E,0x61,0x35,0x57,0xB9,0x86,0xC1,0x1D,0x9E,
0xE1,0xF8,0x98,0x11,0x69,0xD9,0x8E,0x94,0x9B,0x1E,0x87,0xE9,0xCE,0x55,0x28,0xDF,
0x8C,0xA1,0x89,0x0D,0xBF,0xE6,0x42,0x68,0x41,0x99,0x2D,0x0F,0xB0,0x54,0xBB,0x16
]

RCON = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]


# ============ AES UTILS =================

def text_to_hex(text):
    return [format(ord(c), '02X') for c in text]

def to_matrix_4x4(hex_list):
    matrix = [[None]*4 for _ in range(4)]
    for i in range(16):
        row = i % 4
        col = i // 4
        matrix[row][col] = hex_list[i]
    return matrix

def xor_matrices_hex(m1, m2):
    result = [[None]*4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            v1 = int(m1[r][c], 16)
            v2 = int(m2[r][c], 16)
            result[r][c] = format(v1 ^ v2, '02X')
    return result

def rot_word(word):
    return word[1:] + word[:1]

def sub_word(word):
    return [SBOX[b] for b in word]


def words_to_matrix(words):
    matrix = [[0]*4 for _ in range(4)]
    for col in range(4):
        for row in range(4):
            matrix[row][col] = words[col][row]
    return matrix


# ============ KEY EXPANSION WITH LOGS ==============
def key_expansion_logs(key_matrix_hex):
    logs = []
    words = []

    logs.append("\n=== Membentuk W0 - W3 ===")
    for col in range(4):
        w = [key_matrix_hex[row][col] for row in range(4)]
        words.append(w)
        logs.append(f"W{col} = " + " ".join(f"{x:02X}" for x in w))

    for i in range(4, 44):
        temp = words[i-1].copy()
        logs.append(f"\n--- i = {i} ---")
        logs.append("temp = " + " ".join(f"{x:02X}" for x in temp))

        if i % 4 == 0:
            logs.append("RotWord:")
            temp = rot_word(temp)
            logs.append(" -> " + " ".join(f"{x:02X}" for x in temp))

            logs.append("SubWord:")
            temp = sub_word(temp)
            logs.append(" -> " + " ".join(f"{x:02X}" for x in temp))

            rcon = RCON[(i//4)-1]
            temp[0] ^= rcon
            logs.append(f"XOR RCON ({rcon:02X}):")
            logs.append(" -> " + " ".join(f"{x:02X}" for x in temp))

        w_prev = words[i-4]
        new = [(temp[j] ^ w_prev[j]) & 0xFF for j in range(4)]
        words.append(new)
        logs.append(f"W{i} = " + " ".join(f"{x:02X}" for x in new))

    return words, logs



# ======================================================
# =======================  GUI  =========================
# ======================================================

def proses():
    plaintext = entry_plain.get()
    cipherkey = entry_key.get()

    if len(plaintext) < 16:
        plaintext += " " * (16 - len(plaintext))
    elif len(plaintext) > 16:
        plaintext = plaintext[:16]

    if len(cipherkey) < 16:
        cipherkey += " " * (16 - len(cipherkey))
    elif len(cipherkey) > 16:
        cipherkey = cipherkey[:16]

    hex_plain = text_to_hex(plaintext)
    hex_key = text_to_hex(cipherkey)

    m_plain = to_matrix_4x4(hex_plain)
    m_key = to_matrix_4x4(hex_key)
    xor_result = xor_matrices_hex(m_plain, m_key)

    # convert key matrix to bytes for key expansion
    key_bytes = [[int(m_key[r][c], 16) for c in range(4)] for r in range(4)]

    words, logs = key_expansion_logs(key_bytes)

    out = []
    out.append("=== HASIL PRAKTIKUM 8 ===")
    out.append("PLAINTEXT (HEX): " + " ".join(hex_plain))
    out.append("CIPHERKEY (HEX): " + " ".join(hex_key))

    out.append("\nMATRIX PLAINTEXT:")
    for row in m_plain:
        out.append(" ".join(row))

    out.append("\nMATRIX CIPHERKEY:")
    for row in m_key:
        out.append(" ".join(row))

    out.append("\nHASIL XOR (AddRoundKey):")
    for row in xor_result:
        out.append(" ".join(row))

    out.extend(logs)

    out.append("\n=== ROUND KEYS K0 - K10 ===")
    for r in range(11):
        start = r * 4
        end = start + 4
        w = words[start:end]
        mat = words_to_matrix(w)
        out.append(f"\nK{r}:")
        for row in mat:
            out.append(" ".join(f"{x:02X}" for x in row))

    out.append("\nCatatan: ROHANA 230840041")  # FOOTER

    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, "\n".join(out))

def save_file():
    data = text_area.get("1.0", tk.END)
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(data)
        messagebox.showinfo("Berhasil", "File berhasil disimpan!")


# ================= BUILD GUI WINDOW ===================

root = tk.Tk()
root.title("Praktikum 8 - AES Key Expansion")
root.geometry("900x700")
root.configure(bg="#e8f0fe")   # warna soft biru muda


style = ttk.Style()
style.configure("TLabel", font=("Arial", 11), background="#e8f0fe")
style.configure("TButton", font=("Arial", 11))
style.configure("TEntry", font=("Arial", 11))

frm = ttk.Frame(root)
frm.pack(pady=10)

ttk.Label(frm, text="Plaintext (16 karakter):").grid(row=0, column=0, sticky="w")
entry_plain = ttk.Entry(frm, width=40)
entry_plain.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frm, text="Cipher Key (16 karakter):").grid(row=1, column=0, sticky="w")
entry_key = ttk.Entry(frm, width=40)
entry_key.grid(row=1, column=1, padx=10, pady=5)


btn_proses = ttk.Button(root, text="PROSES", command=proses)
btn_proses.pack(pady=10)

text_area = tk.Text(root, height=25, width=100, font=("Consolas", 10))
text_area.pack(pady=10)

btn_save = ttk.Button(root, text="Simpan Hasil ke File", command=save_file)
btn_save.pack(pady=5)

footer = tk.Label(root, text="ROHANA 230840041", font=("Arial", 10, "bold"), bg="#e8f0fe")
footer.pack(pady=5)

root.mainloop()
