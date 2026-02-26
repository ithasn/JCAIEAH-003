import math

jmlHari = 485
sisaHari = jmlHari

# 485 / 360 = 1.34722 => dibulatkan kebawah jadi 1
# variable tahun isinya jadi int 1
tahun = math.floor(sisaHari/360)

# 485 % 360 = 125
# variable sisaHari isinya jadi int 125
sisaHari %= 360

# 125 / 30 = 4.1667 => dibulatkan kebawah jadi 4
# variable bulan isinya jadi int 4
bulan = math.floor(sisaHari/30)

# 125 % 30 = 5
# variable sisaHari isinya jadi int 5
sisaHari %= 30

# 5 / 7 = 0.7143 => dibulatkan kebawah jadi 0
# variable minggu isinya jadi int 0
minggu = math.floor(sisaHari/7)

# 5 % 7 = 5
# variable sisaHari isinya jadi tetap int 5
sisaHari %= 7

# ditampilkan ke terminal
print(str(jmlHari) + ' Hari adalah')
print('{} Tahun'.format(tahun))
print('{} Bulan'.format(bulan))
print('{} Minggu'.format(minggu))
print('{} Hari'.format(sisaHari))
