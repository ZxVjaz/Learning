#persiapan
ulang = 'y'

#perulangan
while ulang == 'y':
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
    elif Nama_Guru == 'thalib':
        Nama_Guru = 'Thalib'
        Hari = 'Jum\'at'
    else:
        Hari = 'Tidak diketahui'

    #Output
    print(f"{'Nama':<15} {'Mapel':<18} {'Jurusan':<18} {'Hari':<18}")
    print(f"{Nama_Guru:<15} {Nama_Mapel:<18} {Jurusan:<18} {Hari:<18}")
    print('=' * 30)

    #Ulang
    ulang = input('Ulang (y/t)?').lower()
#selesai