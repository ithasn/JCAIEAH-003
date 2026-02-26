# usiaAndi + usiaBudi = 49
# rasio usiaAndi dan usiaBudi = 0.4 = 4 / 10 => 4 : 10 => 2 : 5
# rasio usiaAndi = 2 , rasio usiaBudi = 5
# total rasio = 2 + 5 = 7
# usiaAndi = total umur * (rasio usiaAndi / total rasio)
# usiaBudi = total umur * (rasio usiaBudi / total rasio)

totalUmur = 49
ratioAndi = 2
ratioBudi = 5
ratioTotal = 7

usiaAndi = totalUmur * (ratioAndi/ratioTotal)
usiaBudi = totalUmur * (ratioBudi/ratioTotal)

print('Usia Andi sekarang = {}'.format(usiaAndi))
print('Usia Budi sekarang = {}'.format(int(usiaBudi)))

print('Usia Andi 2 tahun lagi = ' + str(usiaAndi + 2))
print('Usia Budi 2 tahun lagi = ' + str(int(usiaBudi) + 2))
