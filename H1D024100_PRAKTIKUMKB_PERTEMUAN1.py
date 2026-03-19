import random
import numpy as np

angka_list = []

for i in range(10):
    angka = random.randint(1, 100)  
    angka_list.append(angka)

print("Daftar angka acak:", angka_list)

rata_rata = np.mean(angka_list)
maksimum = np.max(angka_list)
minimum = np.min(angka_list)

print("Rata-rata:", rata_rata)
print("Nilai maksimum:", maksimum)
print("Nilai minimum:", minimum)

kategori = {
    "tinggi": [],
    "rendah": []
}

for angka in angka_list:
    if angka > rata_rata:
        kategori["tinggi"].append(angka)
    else:
        kategori["rendah"].append(angka)

print("Angka di atas rata-rata:", kategori["tinggi"])
print("Angka di bawah atau sama dengan rata-rata:", kategori["rendah"])