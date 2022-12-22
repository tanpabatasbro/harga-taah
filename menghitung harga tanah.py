# MENGHITUNG HARGA  TANAH
a = int(input("Masukkan Lebar Tanah (m): "))
b = int(input("Masukkan Panjang Tanah (m): "))

harga = 100000 #harga Tanah/meter 

c =  a * b #luas tanah

hargaTotal = c * harga

print(f"Tanah Seluas {c}m adalah {hargaTotal}")
