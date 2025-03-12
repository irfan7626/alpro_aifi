barang_barang = {
    "barang_1" : "Nasi Goreng",
    "barang_2" : "Soto Ayam",
    "barang_3" : "Nasi Padang",
    "barang_4" : "Bubur Ayam",
    "barang_5" : "Ketoprak",
    "barang_6" : "Kupat Tahu",
    "barang_7" : "Gultik",
    "barang_8" : "Gudeg",
    "barang_9" : "Nasi Gila",
    "barang_10" : "Kerak Telor"

}

print(barang_barang)
pilihan_user = int(input("Masukkan nomer untuk memilih menu    "))

if pilihan_user == 1:
    print(barang_barang["barang_1"])
elif pilihan_user == 2:
    print(barang_barang["barang_2"])
elif pilihan_user == 3:
    print(barang_barang["barang_3"])
elif pilihan_user == 4:
    print(barang_barang["barang_4"])
elif pilihan_user == 5:
    print(barang_barang["barang_5"])
elif pilihan_user == 6:
    print(barang_barang["barang_6"])
elif pilihan_user == 7:
    print(barang_barang["barang_7"])
elif pilihan_user == 8:
    print(barang_barang["barang_8"])
elif pilihan_user == 9:
    print(barang_barang["barang_9"])
elif pilihan_user == 10:
    print(barang_barang["barang_10"])
else:
    print("Pilihan tidak valid")