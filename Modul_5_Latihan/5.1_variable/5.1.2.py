#  4. Buatlah 4 variabel dan isi masing-masing dengan data bertipe integer, string, float, dan boolean. Cetak ke layar tipe masing-masing variabel.
#  5. Buatlah 2 variabel berisi integer. Buat variabel ke-3 yang isinya penjumlahan dari 2 variabel pertama.
#  6. Buatlah 1 variabel, isi dengan integer. Ubahlah data integer tersebut menjadi string. Lakukan sebaliknya, yaitu string menjadi integer.
#  7. Buatlah dua variabel yang masing-masing berisi string. Gabungkan kedua string tersebut, lalu cetak ke terminal.

#4
e_integer = 12
e_string = "String"
e_float = 2.2
e_boolean = True

print(type(e_integer))
print(type(e_string))
print(type(e_float))
print(type(e_boolean))

#5
variable_1 = 1
variable_2 = 2
perjumlahan = variable_1 + variable_2
print(perjumlahan)

#6
data_total = 2000
data_user = "350"

print(str(data_total))
print(int(data_user))

#7
nama = "Muhammad Irfan Afifi"
universitas = "Telkom University"
print("halo", nama,"selamat datang di", universitas)