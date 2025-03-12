nama = ["irfan", "afifi", "alpon","chiko","faridh", "dhani", "ravel","alfis","fandi"]

pencarian_user = input("masukkan nama yang ingin dicari:  ")

if pencarian_user in nama:
    print("Nama terdapat pada list")
else:
    print("nama tidak ada pada list")