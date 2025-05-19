# bagian ini berfungsi agar tahun yang digunakan adalah tahun yang sama ketika program ini digunakan
from datetime import datetime
tahun_sekarang = datetime.now().year

print ("Selamat datang di toko tata")
print ("Setiap pembelian makanan dan minuman anda akan mendapat diskon sebesar 10%, dan mendapat diskon sesuai dengan umur anda untuk camilan")

nama = input("Masukkan nama anda! ")
tahunlahir = int(input("Masukkan tahun lahir! "))
# proses untuk menghitung umur user
umur = tahun_sekarang - tahunlahir
# penentuan diskon yang didapat sesuai dengan umur
# diskonFumur = diskon for umur
diskonFumur = umur / 100

# penginputan harga makanan, minuman yang akan di beli
makanan = int(input("Masukkan harga makanan! "))
minuman = int(input("Masukkan harga minuman! "))

# penghitungan harga makanan dan minuman tanpa diskon
totalmakanan = makanan + minuman

# perhitungan diskon default yang didapat sesuai dengan total makanan dan minuman yang di beli
diskonmakanan = totalmakanan * 0.10
totalakhirmakanan = int(totalmakanan - diskonmakanan)
print("selamat untuk makanan dan minuman anda mendapat diskon sebanyak 10%, jadi total makanan dan minuman anda", totalakhirmakanan)

# penginputan harga camilan yang akan di beli
camilan = int(input("Masukkan harga camilan! "))

# perhitungan harga camilan yang kurangi dengan diskon sesuai dengan umur
hargacamilan = camilan * diskonFumur
totalcamilan = int(camilan - hargacamilan)
print("selamat untuk camilan anda mendapat diskon sebanyak",umur, "jadi total makanan dan minuman anda", totalcamilan)

# perhitungan kembali total harga makanan, minuman, dan camilan yang di dapat setelah mendapat diskon
totalakhir= int(totalakhirmakanan + totalcamilan)
print("total yang harus anda bayarkan adalah", totalakhir )

# bagian pembayaran
bayar = int(input("Masukkan total uang yang anda bayarkan "))
kembalian = bayar - totalakhir 
print("total kembalian anda adalah", kembalian)