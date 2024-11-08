var_nilai = {'Riza': 95, 'Hafiz': 85, 'Qohir': 70, 'Faqih': 90}

print(var_nilai)

print('\n------ cetak value ------')
for nilai in var_nilai.values():
    print('Siswa dengan nilai :', nilai)

print('\n------ cetak key ------')
for nama in var_nilai.keys():
    print('Siswa :', nama)

for nama, nilai in var_nilai.items():
    print('\nNama mahasiswa :', nama, '\nNilai :', nilai)
    print('----------------------------------')