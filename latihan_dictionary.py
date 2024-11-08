data_nilai = {'Siti':  90, 'Rahma': 45, 'Ayu': 95,  'Dewi': 90,  'Nur': 92,}

data_nilai ['Dewi'] = 80 #ubah data nilai siswa Dewi menjadi 80
data_nilai.pop ('Nur') #hapus data nilai siswa Nur
del data_nilai ['Ayu'] #hapus data nilai siswa Ayu
#cetak nilai siti
print("Nilai Siti adalah", data_nilai['Siti'])
# cetak semua nilai
print("Nilai semua siswa adalah", data_nilai)
#cetak nilai value saja
for nilai in data_nilai.values():
    print("Nilai siswa adalah", nilai)
#Cetak key(index)nya saja
for key in data_nilai.keys():
    print("Nama siswa adalah", key)
#Cetak all secara manual
for nama,nilai in data_nilai.items():
    ket = ('Lulus','Gagal') [nilai < 80]
    print("siswa :", key , 'dengan nilai', nilai, 'Dinyatakan', ket)

