makanan = {
    "Sate" : 25000,
    "Laksa": 20000,
    "Soto" : 15000,
    "Nasi Goreng" : 16000,
    "Ayam Goreng" : 18.000
}

minuman = {
    "Es Teh" : 5000,
    "Es Jeruk" : 7000,
    "Jus Mangga" : 8000
}

minta_makanan = input("Masukkan nama makanan: ")
minta_minuman = input("masukkan nama minuman: ")

total_harga = makanan.get(minta_makanan) + minuman.get(minta_minuman)

print("Total harga: ", total_harga)