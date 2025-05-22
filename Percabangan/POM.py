#  APLIKASI POM BENSIN 

# buatlah variable yg mana untuk menampung sebuah pertanyaan seberapa banyak liter bahan bakar yg akan dia beli
# dan sebuah variable yg menampung sebuah pertanyaan type bahan bakar yg akan dibeli , 
# ada 5 type bahan bakar (pertamax , pertalite , dexlite , solar dan pertamax turbo) 
# setlah melakukan pemilihan dan  menetapkan berapa liter yg akan di beli , 
# lalu lakukannlah pengecekan terhadap type bahan bakar yg akan di beli untuk nentukan harga yg harus di bayarkan ,
# lalu jika pemilihan type tidak sesuai dengan type yg ada makan munculkan lah type bahan bakar tidak valid , 
# dan untuk rumus harga stiap.type bahan bakar itu silahkan searching pada chrome ada google untuk menentukan harga perliternya  ( contoh : pertalite = 10000 dan  seterusnya ) 
# jadi , jika user memilih type pertalite maka pada variable harga berisi ( liter * pertalite ) dan seterusnya , 
# lalu pada akhir program mnculkan harga yg harus dibayarkan sesuai berapa banyak liter yg akan di beli sesuai harga type bahaan bakar tersebut

print ("*" * 80)
print ("Selamat datang di POM MINI tata")
print ("Kami Menyediakan (pertamax , pertalite , dexlite , solar dan pertamax turbo)")
print ("*" * 80)

# list harga
pertamax = 12400
pertalite = 10000
dexlite = 13350
solar = 6800
pertamax_turbo = 13300

bahanBakar = input("Pilih bahan bakar anda: ").lower()
# .lower() berfungsi agar apa saja yang diinputkan oleh user berubah menjadi huruf kecil semua
# contoh: yang user input "PeRtAmaX" yang akan di terima oleh program "pertamax"

if bahanBakar == "pertamax" or bahanBakar == "pertalite" or bahanBakar == "dexlite" or bahanBakar == "solar" or bahanBakar == "pertamax turbo" :
# kenapa ada percabangan untuk mengecek ini?? 
# Ini berfungsi agar ketika user tidak menginputkan bahan bakar dengan benar program akan berhenti berjalan

    banyak = float(input("Berapa liter yang akan anda beli: "))
    # jika bahan bakar sudah diinputkan dengan benar maka program akan lanjut menanyakan berapa liter yang akan dibeli lebih user

    if bahanBakar == "pertamax":
        total = banyak * pertamax
    elif bahanBakar == "pertalite":
        total = banyak * pertalite
    elif bahanBakar == "dexlite":
        total = banyak * dexlite
    elif bahanBakar == "solar":
        total = banyak * solar
    elif bahanBakar == "pertamax turbo":
        total = banyak * pertamax_turbo
    # kenapa banyak dikali sama pertamax/pertalite/dexlite/solar/pertamax_turbo? kenapa bukan sama angka(harganya)?
    # coba lihat di baris 18 sampai 23 disitu aku nyantumin list harga 
    # nahh bagian itu berfungsi agar ketika ada kenaikan harga kita hanya mengubah disana saja
    # tanpa mengotak-atik code yang ada di dalam percabangan ini
    else:
        print ("bahan bakar invalid, masukkan bahan bakar dengan benar")

    print ("*" * 80)
    # abaikan bagian yang seperti ini

    total= int(total)
    # aku buat konversi ini karena di baris 33 sampai 45 itu float jadi agar tidak ada koma di belakang harga jadi konversi dulu
    # jika kamu kepo jadikan baris 56 menjadi komen (dengan cara ctrl /) saja dan coba run
    
    print ("Total yang harus anda bayarkan Rp.", total)

    bayar = int(input("Inputkan nominal uang yang akan anda bayarkan: "))

    if bayar > total:
        kembalian = bayar - total
        print ("Jadi, kembalian yang anda dapatkan sebanyak Rp.", kembalian)
    elif bayar == total:
        print ("Terima kasih, Uang anda pas")
    elif bayar < total:
        kembalian = total - bayar
        print ("Uang anda kurang sebanyak Rp.", kembalian)
    else:
        print ("nominal yang anda inputkan kurang tepat")

    # dan kenapa bagian bayar ada di if?
    # aku taro di if agar tidak ada traceback
    # info tentang traceback ada di google
else :
    print ("Bahan bakar yang anda inputkan tidak ada")

print ("*" * 80)
