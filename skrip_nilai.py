import pandas as pd
import numpy as np
import random
import time

def ulangan_harian(nilai_akhir, jumlah_uh=5, variasi=3):
    acak = list(np.random.randint(nilai_akhir - variasi, nilai_akhir + variasi, jumlah_uh))
    pembanding = [x + 2*(nilai_akhir - x) for x in acak]
    hasil = sorted(acak + pembanding)[1::2]
    random.shuffle(hasil)
    return hasil

def transform_nilai (daftar, jumlah_uh = 5):
    hasil = [ulangan_harian(x, jumlah_uh) for x in daftar]
    return pd.DataFrame(hasil)

def ambil_data():
    df = pd.read_clipboard()
    kepala = df.columns
    mapel = input(f"Tulis nama mapel {', '.join(list(kepala))}: ")
    while mapel in kepala:
        hasil = df[mapel].tolist()
        jumlah_uh = int(input("tulis jumlah ulangan harian: "))
        transform_nilai(hasil, jumlah_uh).to_clipboard(index=False, header=None)
        print(f"nilai mapel {mapel} sudah disalin", end='\n--------------------------------------------------------\n\n')
        mapel = input(f"Tulis nama mapel {', '.join(list(kepala))}: ")
    print(f'{mapel} tidak ada di tabel')
    time.sleep(5)

ambil_data()