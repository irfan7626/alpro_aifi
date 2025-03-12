angka = (input("masukkan 3 angka: "))
data = angka.split() 
a, b, c = int(data[0]), int(data[1]), int(data[2])

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

nyoba = [a, b, c]

print("Angka yang diurutkan:", nyoba)