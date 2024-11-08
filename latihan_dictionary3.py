umur_teman = {'Rendi':20,'Syifa':19,'Riza':19,'Marsya':18}
print(umur_teman)

print('\n------ cetak value ------')
print('Inilah Beberapa data umur teman saya :')
for umur in umur_teman.values():
    print('>', umur)

print('\n------ cetak key ------')
for teman in umur_teman.keys():
    print('Siswa :', teman)

for teman, umur in umur_teman.items():
    print('\nNama teman saya :', teman, '\nUmurnya :', umur)
    print('----------------------------------')

umur_teman = {'Rendi':20,'Syifa':19,'Riza':19,'Marsya':18}

umur = umur_teman.pop ('Syifa')
print('\nhasil pop',umur)
print('hasil setelah pop',umur_teman)

print('\n--------Hapus Umur -------')
del umur_teman['Riza']
print(umur_teman)
