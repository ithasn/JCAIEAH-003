import mysql.connector
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns


#-----------------Supporting Functions-----------------
def intInput(text):
    while True:
        try:
            x = int(input(text))
            
            if x < 0:
                print('Tidak boleh negatif\n')
                continue

            return x

        except ValueError:
            print('Masukkan bilangan integer\n')

def ytInput(text):
    while True:
        x = input(text).strip().lower()

        if x in ['y','t']:
            return x
        else:
            print('Masukkan hanya "y" atau "t"\n')

def rupiah(x):
    return f"Rp {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def displayTable(df):
    display_df = df.copy().sort_values(by='patientID')
    display_df['biayaRawat'] = display_df['biayaRawat'].apply(rupiah)
    display_df = display_df.rename(columns={
        'patientID':'ID Pasien',
        'nama':'Nama Pasien',
        'jenisKelamin':'Jenis Kelamin',
        'umur':'Umur Pasien',
        'penyakit':'Penyakit',
        'lamaRawat_hari':'Lama Rawat Inap (hari)',
        'biayaRawat':'Biaya Perawatan',
        'jaminan':'Penjaminan'
    })
    display_df.index = display_df.index + 1

    print(tabulate(display_df, headers = 'keys', tablefmt = 'orgtbl'))
    print()


#-----------------SQL Connection Functions-----------------
def readSQL():
    myDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "rumahSakit"
    )

    mycursor = myDB.cursor(dictionary=True)
    query = "select * from pasien"
    mycursor.execute(query)
    result = mycursor.fetchall()

    df = pd.DataFrame(result, columns=mycursor.column_names)
    
    mycursor.close()
    myDB.close()

    return df

def insertSQL(data):
    myDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="rumahSakit"
    )

    mycursor = myDB.cursor()
    query = "INSERT INTO pasien (patientID, nama, jenisKelamin, umur, penyakit, lamaRawat_hari, biayaRawat, jaminan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(query, data)
    myDB.commit()

    print('Data berhasil ditambahkan\n')

    mycursor.close()
    myDB.close()

def deleteSQL(patientID):
    myDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="rumahSakit"
    )

    mycursor = myDB.cursor()
    query = "DELETE FROM pasien WHERE patientID = %s"
    mycursor.execute(query, (patientID,))
    myDB.commit()

    if mycursor.rowcount > 0:
        print('Data berhasil dihapus\n')
    else:
        print('PatientID tidak ditemukan\n')

    mycursor.close()
    myDB.close()

def addPatient(df):
    while True:
        patientID = input('Masukkan ID Pasien (tekan "x" untuk batal): ').upper()

        if patientID == 'X':
            print('Penambahan data baru dibatalkan\n')
            return
        
        if patientID in df['patientID'].values:
            print('ID pasien sudah ada di database\n')
            continue

        nama = input('Masukkan Nama: ').title()

        while True:
            inputJenisKelamin = input('Jenis Kelamin (L/P): ').lower()

            if inputJenisKelamin in ['l', 'p']:
                jenisKelamin = inputJenisKelamin.upper()
                break
            else:
                print('Masukkan hanya: "L", atau "P"\n')

        umur = intInput('Umur: ')
        penyakit = input('Penyakit: ').title()
        lamaRawat_hari = intInput('Lama Rawat (hari): ')
        biayaRawat = intInput('Biaya Rawat: ')

        while True:
            inputJaminan = input('Jaminan (BPJS/Asuransi/Umum): ').lower()

            if inputJaminan in ['bpjs', 'asuransi', 'umum']:
                jaminan = inputJaminan.title()
                break
            else:
                print('Masukkan hanya: "BPJS", "Asuransi", atau "Umum"\n')

        data = (
            patientID,
            nama,
            jenisKelamin,
            umur,
            penyakit,
            lamaRawat_hari,
            biayaRawat,
            jaminan
        )

        print("\nKonfirmasi Data Pasien yang ingin ditambahkan")
        print(f"ID            : {patientID}")
        print(f"Nama          : {nama}")
        print(f"Jenis Kelamin : {jenisKelamin}")
        print(f"Umur          : {umur}")
        print(f"Penyakit      : {penyakit}")
        print(f"Lama Rawat    : {lamaRawat_hari} hari")
        print(f"Biaya Rawat   : {rupiah(biayaRawat)}")
        print(f"Jaminan       : {jaminan}")

        confirm = ytInput('\nApakah anda yakin data sudah benar? (y/t): ')
        
        if confirm == 'y':
            insertSQL(data)
        else:
            print('\nBatal ditambahkan\n')

        break

def deletePatient(df):
    displayTable(df)

    while True:
        patientID = input('Masukkan Patient ID yang ingin dihapus (tekan "x" untuk batal): ').strip().upper()

        if patientID == 'X':
            print('Penghapusan dibatalkan\n')
            return

        if patientID not in df['patientID'].values:
            print('Patient ID tidak ditemukan\n')
            continue

        print("\nData pasien yang akan dihapus:")
        displayTable(df[df['patientID'] == patientID])

        confirm = ytInput("\nApakah anda yakin ingin menghapus data ini? (y/t): ")

        if confirm == 'y':
            deleteSQL(patientID)
        else:
            print('Batal dihapus\n')
        
        break


#-----------------Statistics Functions-----------------
def showStatistics(df):
    print('Tunjukkan statistik:')
    print('1. Umur Pasien')
    print('2. Lama Rawat Inap Pasien')
    print('3. Biaya Perawatan Pasien\n')

    while True:
        while True:
            pilihan = input('Masukkan nomor kolom yang ingin dihitung rata-ratanya (tekan "x" untuk batal): ')
            if pilihan == 'x':
                print('Tampilan statistik dibatalkan\n')
                return

            print()
            if pilihan == '1':
                print(tabulate(df[['umur']].describe().T[['count','mean','min','max','std']].rename(index={'umur':'Umur Pasien'}), headers='keys', tablefmt='orgtbl'))
                print()
                break
            elif pilihan == '2':
                print(tabulate(df[['lamaRawat_hari']].describe().T[['count','mean','min','max','std']].rename(index={'lamaRawat_hari':'Lama Rawat Inap (hari)'}), headers='keys', tablefmt='orgtbl'))
                print()
                break
            elif pilihan == '3':
                stats = df[['biayaRawat']].describe().T[['count','mean','min','max','std']]
                stats = stats.rename(index={'biayaRawat':'Biaya Perawatan'})

                for col in ['mean','min','max','std']:
                    stats[col] = stats[col].apply(rupiah)

                print(tabulate(stats, headers='keys', tablefmt='orgtbl'))
                print()
                break
            else:
                print('Masukkan sesuai nomor yang ada\n')
                continue

        repeat = ytInput('Anda ingin menghitung rata-rata yang lain? (y/t): ')
        
        if repeat == 'y':
            continue
        else:
            break


#-----------------Data Visualization Functions-----------------
def pieChart(df, var, chartTitle):
    df[var].value_counts().plot(
        kind='pie',
        autopct='%1.1f%%'
    )
    plt.title(chartTitle)
    plt.ylabel('')
    plt.show()

def barChart(df, var, xLabel, yLabel, chartTitle):
    plt.figure()

    counts, bins, patches = plt.hist(
        df[var],
        bins=10,
        rwidth=0.8,
        edgecolor='black'
    )
    
    for count, patch in zip(counts, patches):
        x = patch.get_x() + patch.get_width() / 2
        y = patch.get_height()
        plt.text(x, y, int(count), ha='center', va='bottom')

    plt.title(chartTitle)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()

def stackedBarChart(df, var, stackVar, xLabel, yLabel, chartTitle):
    plt.figure()

    stackList = df[stackVar].unique()

    data = [
        df[df[stackVar] == p][var]
        for p in stackList
    ]

    plt.hist(
        data,
        bins=10,
        stacked=True,
        label=stackList,
        edgecolor='black',
        rwidth=0.9
    )

    plt.title(chartTitle)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    plt.legend(
        bbox_to_anchor=(1.05, 1),
        loc='upper left',
        borderaxespad=0.
    )

    plt.show()

def stackedBarChart2(df, xVar, stackedVar, xLabel, yLabel, chartTitle):
    ct = pd.crosstab(df[xVar], df[stackedVar])

    ax = ct.plot(
        kind='bar',
        stacked=True,
        color=['skyblue','lightpink']
    )

    plt.title(chartTitle)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    for container in ax.containers:
        ax.bar_label(container)

    plt.show()

def boxPlot(df, xVar, yVar, chartTitle):
    sns.boxplot(data=df, x=xVar, y=yVar)
    plt.xticks(rotation=45)
    plt.title(chartTitle)
    plt.show()

def scatterPlot(df, xVar, yVar, sizeVar, colorVar, shapeVar, chartTitle):
    plt.figure(figsize=(8,6))

    ax = sns.scatterplot(
        data=df,
        x=xVar,
        y=yVar,
        size=sizeVar,
        hue=colorVar,
        style=shapeVar,
        sizes=(50, 300)
    )

    plt.title(chartTitle)

    plt.legend(
        bbox_to_anchor=(1.05, 1),
        loc='upper left',
        borderaxespad=0.
    )

    plt.tight_layout()
    plt.show()

def visualizeData(df):

    while True:

        print('Pilih Visualisasi Data yang Ingin Ditampilkan:')
        print('1. Distribusi Jenis Kelamin Pasien')
        print('2. Distribusi Penyakit Pasien')
        print('3. Distribusi Umur Pasien')
        print('4. Distribusi Lama Rawat Inap Pasien')
        print('5. Distribusi Total Biaya Perawatan Pasien')
        print('6. Distribusi Penyakit berdasarkan Jenis Kelamin')
        print('7. Distribusi Umur pada Setiap Penyakit')
        print('8. Distribusi Biaya Perawatan terhadap Lama Perawatan\n')

        pilihan = input('Pilih visualisasi (tekan "x" untuk batal): ')

        if pilihan == 'x':
            print('Visualisasi data dibatalkan\n')
            return

        if pilihan == '1':
            pieChart(
                df,
                var='jenisKelamin',
                chartTitle='Distribusi Jenis Kelamin Pasien'
                )

        elif pilihan == '2':
            pieChart(
                df,
                var='penyakit',
                chartTitle='Distribusi Penyakit Pasien'
                )

        elif pilihan == '3':
            barChart(
                df,
                var='umur',
                xLabel='Umur',
                yLabel='Jumlah Pasien',
                chartTitle='Distribusi Umur Pasien'
                )
            
            stackedBarChart(
                df,
                var='umur',
                stackVar='penyakit',
                xLabel='Umur',
                yLabel='Jumlah Pasien',
                chartTitle='Distribusi Umur Pasien (Detail Penyakit)'
                )   

        elif pilihan == '4':
            barChart(
                df,
                var='lamaRawat_hari',
                xLabel='Hari',
                yLabel='Jumlah Pasien',
                chartTitle='Distribusi Lama Rawat Inap Pasien'
                )
            
            stackedBarChart(
                df,
                var='lamaRawat_hari',
                stackVar='penyakit',
                xLabel='Hari',
                yLabel='Jumlah Pasien',
                chartTitle='Distribusi Lama Rawat Inap Pasien (Detail Penyakit)'
                )        

        elif pilihan == '5':
            barChart(
                df,
                var='biayaRawat',
                xLabel='Biaya (Juta)',
                yLabel='Jumlah Pasien',
                chartTitle='Distribusi Total Biaya Perawatan Pasien'
                )
            
            stackedBarChart(
                df,
                var='biayaRawat',
                stackVar='penyakit',
                xLabel='Biaya (Juta)',
                yLabel='Jumlah Pasien',
                chartTitle='Distribusi Total Biaya Perawatan Pasien (Detail Penyakit)'
                )

        elif pilihan == '6':
            stackedBarChart2(
                df,
                xVar='penyakit',
                stackedVar='jenisKelamin',
                xLabel='Penyakit',
                yLabel='Jumlah Pasien', 
                chartTitle='Distribusi Penyakit berdasarkan Jenis Kelamin'
                )
        
        elif pilihan =='7':
            boxPlot(
                df,
                xVar='penyakit',
                yVar='umur',
                chartTitle='Distribusi Umur Pada Setiap Penyakit'
                )
        
        elif pilihan == '8':
            scatterPlot(
                df,
                xVar='lamaRawat_hari',
                yVar='biayaRawat',
                sizeVar='umur',
                colorVar='penyakit',
                shapeVar='jaminan',
                chartTitle='Distribusi Biaya Perawatan terhadap Lama Perawatan'
                )

        else:
            print('Pilihan tidak valid')

        repeat = ytInput('\nAnda ingin melihat visualisasi data yang lain? (y/t): ')

        if repeat == 'y':
            continue
        else:
            print('Kembali ke menu utama\n')
            break


#-----------------Main Menu-----------------
def mainMenu():
    dataPasien = readSQL()
    while True:
        print('\n--------------------------------------------------------')
        print('Selamat Datang di Aplikasi Pendataan Pasien Rumah Sakit\n')
        print('Pilih menu:')
        print('1. Tampilkan daftar pasien')
        print('2. Tunjukkan statistik')
        print('3. Tampilkan visualisasi data statistik')
        print('4. Tambah data pasien baru')
        print('5. Hapus data pasien')
        print('6. Keluar dari program\n')

        inputMenu = input('Masukkan nomor menu yang ingin dijalankan: ')
        print()

        if inputMenu == '1':
            displayTable(dataPasien)
        elif inputMenu == '2':
            showStatistics(dataPasien)
        elif inputMenu == '3':
            visualizeData(dataPasien)
        elif inputMenu == '4':
            addPatient(dataPasien)
            dataPasien = readSQL()
        elif inputMenu == '5':
            deletePatient(dataPasien)
            dataPasien = readSQL()
        elif inputMenu == '6':
            break
        else:
            print('Masukkan sesuai nomor yang ada\n')

mainMenu()

            
