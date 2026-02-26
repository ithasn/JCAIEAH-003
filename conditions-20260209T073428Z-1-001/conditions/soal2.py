massa = int(input("Masukkan Massa(kg) : "))
tinggi = int(input("Masukkan Tinggi(cm) : "))

IMT = massa / ((tinggi/100)**2)

text = ""

if(IMT < 18.5) :
    text = "BERAT BADAN KURANG!"
elif(IMT >= 18.5 and IMT <= 24.9) :
    text = "BERAT BADAN IDEAL!"
elif(IMT >= 25.0 and IMT <= 29.9) :
    text = "BERAT BADAN BERLEBIH!"
elif(IMT >= 30.0 and IMT <= 39.9) :
    text = "BERAT BADAN SANGAT BERLEBIH!"
else :
    text = "OBESITAS!"

print("Massa " + str(massa) + " kg & tinggi " + str(tinggi/100) + " m")
print("IMT = " + str(IMT) + ", " + text)