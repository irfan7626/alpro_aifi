nama = input("Masukkan 10 nama: ")
nama = nama.split()

kelompok = {}

huruf = nama[0][0]
if huruf in kelompok:
    kelompok[huruf]. append(nama[0])
else:
    kelompok[huruf] = [nama[0]]

huruf = nama[1][0]
if huruf in kelompok:
    kelompok[huruf]. append(nama[1])
else:
    kelompok[huruf] = [nama[1]]

print(huruf)
print(kelompok)