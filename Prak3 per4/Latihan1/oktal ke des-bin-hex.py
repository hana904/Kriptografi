def konversi_oktal():
    oktal = input("Masukkan bilangan oktal: ")
    desimal = int(oktal, 8)
    biner = bin(desimal)[2:]
    heksadesimal = hex(desimal)[2:]
    
    print(f"\nBilangan Oktal       : {oktal}")
    print(f"Bilangan Desimal     : {desimal}")
    print(f"Bilangan Biner       : {biner}")
    print(f"Bilangan Heksadesimal: {heksadesimal.upper()}")

konversi_oktal()
