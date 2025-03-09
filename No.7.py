import random

# Input kalimat dari user
kalimat = input("Masukkan kalimat: ")

# Memisahkan kalimat menjadi list kata-kata
kata_kata = kalimat.split()

# Mengacak list kata-kata
random.shuffle(kata_kata)

# Menggabungkan kembali kata-kata yang sudah diacak menjadi kalimat
kalimat_acak = " ".join(kata_kata)

# Menampilkan kalimat yang sudah diacak
print("Kalimat acak:", kalimat_acak)
