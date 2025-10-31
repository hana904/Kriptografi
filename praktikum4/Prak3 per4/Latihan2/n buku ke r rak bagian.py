import itertools

def susun_buku(n, r):
    buku = [f"Buku{i+1}" for i in range(n)]
    rak = [f"Rak{j+1}" for j in range(r)]
    
    hasil = list(itertools.product(rak, repeat=n))
    
    print(f"\nTotal cara menyusun {n} buku di {r} rak = {len(hasil)} cara\n")
    for i, susunan in enumerate(hasil, start=1):
        pasangan = [f"{buku[j]}->{susunan[j]}" for j in range(n)]
        print(f"{i}. {', '.join(pasangan)}")

# Contoh penggunaan
n = int(input("Masukkan jumlah buku: "))
r = int(input("Masukkan jumlah rak: "))
susun_buku(n, r)
