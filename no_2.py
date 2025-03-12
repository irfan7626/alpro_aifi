import random

print("Halo Dunia \n"
"selamat datang di permainan tebak angka\n"
"semoga beruntung!!\n"
"silahkan")

tebak_komputer = random.randint(0, 100)
tebak_user = int(input("Pilih angka dari 0 sampai 100: "))

selisih = abs(tebak_komputer - tebak_user)

if selisih < 10:
    print("Menang")
elif 10 < selisih < 30:
    print("hampir")
else:
    print("jauh")