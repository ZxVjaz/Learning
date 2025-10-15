#Persiapan
no = 1
#perulangan
while True:
    #Pembukaan
    print('=' * 30)
    while True:
        Nama_Guru = input('Nama Guru:').lower().replace(' ', '')
        if Nama_Guru == 'ramdani' or Nama_Guru == 'atiks' or Nama_Guru == 'indri' or Nama_Guru == 'faizal' or Nama_Guru == 'tholib':
            break
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
    else:
        Nama_Guru = 'Tholib'
        Hari = 'Jum\'at'

    #Output
    print(no, Nama_Guru, Nama_Mapel, Jurusan, Hari)
    print('=' * 30)
    
    #No +
    no += 1

    #Ulang
    ulang = input('Ulang (y/t)?').lower()
    if ulang == 't':
        break
#selesai