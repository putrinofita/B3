#  ZAKAT( MEDIUM = AGAK SULIT )
# - VARIABEL = HARTA (INPUT)  , HUTANG (INPUT) , TOTAL KEKAYAAN
# - RUMUS = TOTAL KEKAYAAN * 2.5 / 100 
# - PENGECAKAN (IF , ELIF ,ELSE) = SUDAH 1 TAUN APA TIDAK (STRING) , DIATAS 100JT (INTEGER)
# - PRINT = ANDA WAJIB BERZAKAT SEBESAR , ANDA TIDAK WAJIB BERZAKAT

Harta = int(input("Berapa Kekayaan anda: "))
Hutang = int (input ("Berapa hutang anda: "))

lamaharta = input(" Apakah harta yang kamu miliki sudah  genap 1 tahun ? (iya / tidak):")

totalKekayaan = Harta - Hutang

if lamaharta == "iya":
    if totalKekayaan >= 100000000:
        zakat = int (totalKekayaan * 2.5 / 100)
        print ("Zakat yang wajib anda bayarkan sebesar", zakat )
    else :
        print ("Anda tidak wajib berzakat, harta anda belum mencapai target")

else :
    print ("Harta anda belum mencapai 1 tahun, sabar tapi kalo mau zakat sesuai kemauan anda silahkan")