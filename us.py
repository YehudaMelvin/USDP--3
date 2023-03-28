from os import replace, system

def menu ():
    system('cls')

    print('======== KONVERSI BILANGAN ========')
    print('')
    print('1|Desimal')
    print('2|Biner')
    print('3|Oktal')
    print('4|Hexadecimal')
    print('5|ASCII')
    print('6|Leave..')
    print('')
    pick = input('Pilih Nomor : ')
    if pick == '1':
        desimal()
    elif pick == '2':
        biner()
    elif pick == '3':
        oktal()
    elif pick == '4':
        hexa()
    elif pick == '5':
        Ascii()
    elif pick == '6':
        leave()
    else:
        error()

def error():
    print('Inputan anda tidak tertera')
    menu()

def desimal():
    try:
        angka = int(input('Nilai Desimal : '))
    except ValueError:
        err = input('Bilangan Salah!')
        desimal()
    biner = bin(angka).replace("0b","")
    oktal = oct(angka).replace("0o","")
    hexa = hex(angka).replace("0h","")

    print("========= HASIL ==========")
    print("Biner : ", biner)
    print("Oktal : ", oktal)
    print("Hexadecimal : ", hexa)
    print("======== SELESAI ========")
    print("")
    ulangi = input("Apakah anda ingin mengulang konversi (y/t)")
    if ulangi == "y" or ulangi == "Y":
        desimal()
    else:
        menu()

def biner():
    try:
        angka = int(input('Nilai Biner : '), 2)
    except ValueError:
        err = input('Bilangan Salah!')
        biner()
    oktal = oct(angka).replace("0o", "")
    hexa = hex(angka).replace("0h", "")

    print("========= HASIL ==========")
    print("Decimal : ", angka)
    print("Oktal : ", oktal)
    print("Hexadecimal : ", hexa)
    print("======== SELESAI ========")
    print("")
    ulangi = input("Apakah anda ingin mengulang konversi (y/t)")
    if ulangi == "y" or ulangi == "Y":
        biner()
    else:
        menu()

def oktal():
    try:
        angka = int(input("Nilai Oktal : "), 8)
    except ValueError:
        err = input("Bilangan Salah!")
        oktal()
    biner = bin(angka).replace("0b", "")
    hexa = hex(angka).replace("0h", "")

    print("========= HASIL ==========")
    print("Decimal : ", angka)
    print("Biner : ", biner)
    print("Hexadecimal : ", hexa)
    print("======== SELESAI ========")
    print("")
    ulangi = input("Apakah anda ingin mengulang konversi (y/t)")
    if ulangi == "y" or ulangi == "Y":
        oktal()
    else:
        menu()

def hexa():
    try:
        angka = int(input("Bilangan Hexadesimal : "), 16)
    except ValueError:
        err = input("Bilangan Salah!")
        hexa()
    biner = bin(angka).replace("0b", "")
    oktal = oct(angka).replace("0o", "")

    print("========= HASIL ==========")
    print("Decimal : ", angka)
    print("Biner : ", biner)
    print("Oktal : ", oktal)
    print("======== SELESAI ========")
    print("")
    ulangi = input("Apakah anda ingin mengulang konversi (y/t)")
    if ulangi == "y" or ulangi == "Y":
        hexa()
    else:
        menu()

def Ascii():
    try:
        string = input("Masukan Sebuah String Ke Dalam Kolom : ")
        ascii_values = [ord(character) for character in string]
    except ValueError:
        err = input("String Salah!")
        Ascii()

    print("========= HASIL ==========")
    print("Ascii : ", ascii_values)
    print("======== SELESAI ========")
    print("")
    ulangi = input("Apakah anda ingin mengulang konversi (y/t)")
    if ulangi == "y" or ulangi == "Y":
        Ascii()
    else:
        menu()

def leave():
    print("====Terimakasih :)====")
    exit()

menu()
