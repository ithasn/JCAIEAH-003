# Dua mobil a dan b melaju berlawanan arah dan akan bertabrakan.
# Kita dapat hitung waktunya dengan menjumlahkan kecepatan dari kedua kendaraan tersebut.
# Lalu kemudian cari tahu dengan total kecepatan yang dimiliki,
# berapa waktu yang dibutuhkan untuk menempuh jarak tertentu

# 60 km/h + 40 km/h = 100 km/h
# Dengan kecepatan 100 km/h. Berapa waktu yang dibutuhkan untuk menempuh jarak 120 km?
# 120 / 100 = 1.2 jam
# 1.2 * 60 = 72 menit => 60 menit + 12 menit
# 9:00 => 10:12
# waktu bertemu jam 10 menit ke 12

import math 

jamAwal = 9
jarakKM = 120
kecepatanTotalKMperJam = 100
kecepatanTotalKMperDetik = kecepatanTotalKMperJam/3600

DetikTotal = jarakKM / kecepatanTotalKMperDetik
lamaJam = math.floor(DetikTotal / 3600)
lamaMenit = math.floor((DetikTotal%3600)/60)
lamaDetik = math.floor((DetikTotal%3600)%60)

print('Lama waktu ' +  str(lamaJam) + ' jam, ' + str(lamaMenit) + ' menit, ' + str(lamaDetik) + ' detik')
print('Tabraknya pukul {}:{}:{}'.format(jamAwal + lamaJam,lamaMenit,lamaDetik))
