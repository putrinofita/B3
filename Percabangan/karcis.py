print("Selamat datang di Bioskop tata")
usia = int(input("Silahkan masukkan usia anda: "))
hari = input("Masukkan hari yang akan anda kunjungi: ")
biaya = 0

if usia < 5:
    print ("Selamat biaya yang harus anda bayarkan Rp.0")
elif usia >= 5 and usia <= 12 :
    biaya = 20000
    print ("Selamat biaya yang harus anda bayarkan Rp.", biaya)
elif usia >= 13 and usia <= 59 :
    biaya = 45000
    print ("Selamat biaya yang harus anda bayarkan Rp.", biaya)
elif usia > 60:
    biaya = 35000
    print ("Selamat biaya yang harus anda bayarkan Rp.", biaya)
else:
    print ("umur tidak valid")