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


print ("Selamat datang di POM MINI tata")
print ("Kami Menyediakan (pertamax , pertalite , dexlite , solar dan pertamax turbo)")

bahanBakar = input("Pilih bahan bakar anda: ").lower()
if bahanBakar == "pertamax" or bahanBakar == "pertalite" or bahanBakar == "dexlite" or bahanBakar == "solar" or bahanBakar == "pertamax turbo" :
    banyak = float(input("Berapa liter yang akan anda beli: "))

    if bahanBakar == "pertamax":
        total = banyak * 12_000
    elif bahanBakar == "pertalite":
        total = banyak * 14_000
    elif bahanBakar == "dexlite":
        total = banyak * 16_000
    elif bahanBakar == "solar":
        total = banyak * 18_000
    else:
        total = banyak * 19_000

    total= int(total)
    
    print ("Total yang harus anda bayarkan Rp.", total)

    bayar = int(input("Inputkan nominal uang yang akan anda bayarkan: "))

    kembalian = total - bayar

    print ("Jadi, kembalian yang anda dapatkan sebanyak Rp.", kembalian)

else :
    print ("Bahan bakar yang anda inputkan tidak ada")