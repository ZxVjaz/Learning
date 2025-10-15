#Pembukaan
print('=' * 30)
Nama_Guru = input('Nama Guru:').lower().replace(' ', '')
Nama_Mapel = input('Nama Mapel:')
Jurusan = input('Jurusan:')
print('=' * 30)

#Proses

if Nama_Guru == 'ramdani':
    Nama_Guru = 'Ramdani'
    Hari = 'Senin'
elif Nama_Guru == 'atiks':
    Nama_Guru = 'Atik S'
    Hari = 'Selasa'
elif Nama_Guru == 'indri':
    Nama_Guru = 'Indri'
    Hari = 'Rabu'
elif Nama_Guru == 'faizal':
    Nama_Guru = 'Faizal'
    Hari = 'Kamis'
elif Nama_Guru == 'tholib':
    Nama_Guru = 'Tholib'
    Hari = 'Jum\'at'
else:
    Hari = 'Tidak diketahui'

#Output
print(Nama_Guru, Nama_Mapel, Jurusan, Hari)