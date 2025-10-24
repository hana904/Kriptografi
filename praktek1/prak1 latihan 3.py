# Latihan 3: Menghitung Nilai Akhir Akademik

def hitung_nilai_akhir(sikap, tugas, uts, uas):
    # bobot sesuai ketentuan
    total = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)
    return total

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

# --- Program utama ---
print("=== Program Menghitung Nilai Akhir Akademik ===")

sikap = float(input("Masukkan nilai Sikap/Kehadiran (0-100): "))
tugas = float(input("Masukkan nilai Tugas (0-100): "))
uts   = float(input("Masukkan nilai UTS (0-100): "))
uas   = float(input("Masukkan nilai UAS (0-100): "))

total_nilai = hitung_nilai_akhir(sikap, tugas, uts, uas)
huruf, bobot = konversi_nilai(total_nilai)

print("\n=== Hasil Akhir ===")
print(f"Total Nilai Akhir : {total_nilai:.2f}")
print(f"Nilai Huruf       : {huruf}")
print(f"Bobot Nilai       : {bobot}")

if total_nilai >= 56:
    print("Keterangan        : LULUS")
else:
    print("Keterangan        : TIDAK LULUS")
