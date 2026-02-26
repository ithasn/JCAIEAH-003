print('Pengecheckan Ujian')

nilai = int(input("Masukkan nilai : "))
grade = ''

if(nilai >= 90 and nilai <= 100) :
    grade = 'A'
elif(nilai >= 80 and nilai <= 89) :
    grade = 'B'
elif(nilai >= 70 and nilai <= 79) :
    grade = 'C'
elif(nilai >= 60 and nilai <= 69) :
    grade = 'D'
elif(nilai >= 0 and nilai <= 59) :
    grade = 'F'
else :
    grade = 'Nilai harus berada pada jarak 0-100 saja'

print('Grade = {}'.format(grade))