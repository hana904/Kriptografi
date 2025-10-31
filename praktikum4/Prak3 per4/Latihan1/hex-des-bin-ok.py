def konversi_hexadesimal():
    heksa = input("Masukkan bilangan heksadesimal: ")
    desimal = int(heksa, 16)
    biner = bin(desimal)[2:]
    oktal = oct(desimal)[2:]
    
    print(f"\nBilangan Heksadesimal: {heksa.upper()}")
    print(f"Bilangan Desimal     : {desimal}")
    print(f"Bilangan Biner       : {biner}")
    print(f"Bilangan Oktal       : {oktal}")

konversi_hexadesimal()
