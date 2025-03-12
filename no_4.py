angka1 = int(input("masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
operasi = int(input("Pilih operasi: "))

if operasi == 1:
    print(angka1 + angka2)
elif operasi == 2:
    print(angka1 - angka2)
elif operasi == 3:
    print(angka1*angka2)
elif operasi == 4:
    print (int(angka1/angka2))
else:
    print("Invalid, harap coba kembali")