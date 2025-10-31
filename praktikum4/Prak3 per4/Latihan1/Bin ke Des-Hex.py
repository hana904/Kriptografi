def konversi_biner():
    biner = input("Masukkan bilangan biner: ")
    desimal = int(biner, 2)
    heksadesimal = hex(desimal)[2:]
    
    print(f"\nBilangan Biner     : {biner}")
    print(f"Bilangan Desimal   : {desimal}")
    print(f"Bilangan Heksadesimal : {heksadesimal.upper()}")

konversi_biner()
