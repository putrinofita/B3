print("Selamat datang di parkir me")
print("silahkan masukkan berapa lama anda parkir")
lamaparkir = int (input("Lama parkir: "))
biaya = 0

if lamaparkir <= 0:
    print ("Waktu tidak valid, waktu harus 1 jam atau lebih")
elif lamaparkir == 1 :
    biaya = 5000
elif lamaparkir <= 3 :
    biaya = 5000 + (lamaparkir - 1 ) * 3000
else:
        biaya = 5000 + (2 * 3000) + (lamaparkir - 3) * 2000

if lamaparkir >= 6:
        diskon = biaya * 0.10
        biaya = biaya - diskon

print("Biaya parkir anda sebesar Rp", int(biaya))