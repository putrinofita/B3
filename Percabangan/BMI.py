beratbadan = float(input("Masukkan berat badan anda (kg): "))
tinggibadan = float(input("Masukkan tinggi badan anda (m): "))

BMI = beratbadan // (tinggibadan ** 2)

print ("Skor BMI anda adalah", BMI)

if BMI <= 20.6:
    print ("Kurus")
elif BMI >= 20.7 and BMI <= 26.4:
    print ("Normal")
elif BMI >= 26.5 and BMI <= 30.9:
    print ("Gemuk")
elif BMI >= 31.0 and BMI <= 45.2:
    print ("Obesitas")
else :
    print ("Bahaya")