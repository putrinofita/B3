print ("-" * 70)
print ("Selamat Datang di layanan administrasi universitas ...")
print ("Kini kami menyediakan beasiswa untuk mahasiswa berprestasi")
print ("Ayo cek kesempatanmu sekarang!!!")
print ("-" * 70)
ipk = float (input("IPK: "))

if ipk > 4:
    print ("IPK tidak valid")
elif ipk >= 3.8:
        status = input("Apakah anda aktif di organisasi atau tidak (iya/tidak): ").lower() .strip()
        if status == "iya":
            print ("Selamat anda salah satu orang yang berhak mendapat beasiswa")
        elif status == "tidak":
            print ("Selamat anda salah satu orang yang berhak mendapat beasiswa")
        else:
            print("status keaktifan anda tidak valid")

elif ipk >= 3.5:
    penghasilan_ortu = int(input("Penghasilan orang tua (contoh: 4000000): Rp."))
    if penghasilan_ortu <= 4_000_000:
        
        status = input("Apakah anda aktif di organisasi atau tidak (iya/tidak): ").lower() .strip()
        if status == "iya":
            print ("Selamat anda salah satu orang yang berhak mendapat beasiswa")
        elif status == "tidak":
            print("status keaktifan anda tidak memenuhi syarat")
        else:
            print("status keaktifan anda tidak valid")

    elif penghasilan_ortu <= 3_500_000:
        status = input("Apakah anda aktif di organisasi atau tidak (iya/tidak): ").lower() .strip()
        if status == "iya":
            print ("Selamat anda salah satu orang yang berhak mendapat beasiswa")
        elif status == "tidak":
            print("status keaktifan anda tidak memenuhi syarat")
        else:
            print("status keaktifan anda tidak valid")

    else:
        print("untuk mendapatkan beasiswa minimal penghasilan orang tua sebesar Rp.4.000.000")

else:
    print("untuk mendapatkan beasiswa, ipk minimal 3.5")

print ("Terima Kasih Telah Menggunakan Layanan Kami")
print ("-" * 70)
