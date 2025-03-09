import random
# List huruf vokal
vokal = ['a', 'e', 'i', 'o', 'u']

# List huruf konsonan
konsonan = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
            'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

# Fungsi untuk menghasilkan nama acak
def generate_random_name():
    # Huruf ke-1: konsonan
    huruf1 = random.choice(konsonan)
    # Huruf ke-2: vokal
    huruf2 = random.choice(vokal)
    # Huruf ke-3: konsonan
    huruf3 = random.choice(konsonan)
    # Huruf ke-4: vokal
    huruf4 = random.choice(vokal)
    # Huruf ke-5: konsonan
    huruf5 = random.choice(konsonan)
    
    # Gabungkan semua huruf menjadi nama
    nama = huruf1 + huruf2 + huruf3 + huruf4 + huruf5
    return nama

# Menghasilkan dan menampilkan nama acak
random_name = generate_random_name()
print("Nama acak yang dihasilkan:", random_name)