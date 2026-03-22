create database rumahSakit;
use rumahSakit;

create table pasien (
	patientID varchar(5) primary key,
    nama varchar(255),
    jenisKelamin varchar(1),
    umur int,
    penyakit varchar(255),
    lamaRawat_hari int,
    biayaRawat float,
    jaminan varchar(50)
    );

INSERT INTO pasien VALUES
('P001','Andi Pratama','L',34,'Demam Berdarah',4,3200000,'BPJS'),
('P002','Siti Rahma','P',29,'Tipes',5,2800000,'BPJS'),
('P003','Budi Santoso','L',45,'Diabetes',3,4500000,'Asuransi'),
('P004','Maya Putri','P',52,'Hipertensi',2,1700000,'Umum'),
('P005','Rudi Hartono','L',38,'Asma',3,2100000,'Umum'),
('P006','Lina Kartika','P',26,'Tipes',4,2900000,'BPJS'),
('P007','Dedi Kurniawan','L',60,'Jantung',7,8500000,'Asuransi'),
('P008','Fitri Aisyah','P',31,'Demam Berdarah',4,3400000,'BPJS'),
('P009','Agus Saputra','L',48,'Diabetes',5,5100000,'Asuransi'),
('P010','Nanda Putra','L',22,'Asma',2,1500000,'Umum'),
('P011','Rina Melati','P',41,'Hipertensi',3,2200000,'BPJS'),
('P012','Wahyu Nugroho','L',37,'Tipes',4,2700000,'BPJS'),
('P013','Dewi Lestari','P',33,'Demam Berdarah',5,3800000,'Asuransi'),
('P014','Hendra Gunawan','L',55,'Jantung',6,7900000,'Asuransi'),
('P015','Sari Oktavia','P',27,'Asma',3,2000000,'Umum'),
('P016','Rizky Maulana','L',30,'Tipes',4,2600000,'BPJS'),
('P017','Nurhaliza','P',36,'Diabetes',5,4800000,'Asuransi'),
('P018','Fajar Ramadhan','L',40,'Hipertensi',3,2300000,'Umum'),
('P019','Putri Maharani','P',24,'Demam Berdarah',4,3100000,'BPJS'),
('P020','Yudi Saputra','L',50,'Jantung',6,7200000,'Asuransi');

select * from pasien;