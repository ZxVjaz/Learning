#Mulai
print("=" * 50)
print("PROGRAM PARKIR")
print("=" * 50)

#Input
Nopol = input('MASUKKAN NOMOR POLISI KENDARAAN ANDA (CONTOH: B 2774 KCA): ')
JenisKendaraan = input('PILIH JENIS KENDARAAN \n' \
                        '1. MOTOR \n' \
                        '2. MOBIL \n' \
                        'MASUKKAN PILIHAN ANDA (1/2): ')
JamMasuk = int(input('JAM MASUK (24 JAM): '))
JamKeluar = int(input('JAM KELUAR (24 JAM): '))

#Seleksi
if JenisKendaraan == '1':
    Harga = 3000
else:
    Harga = 5000
    
#Proses
Total = (JamKeluar - JamMasuk) * Harga

#Output
print('=' * 50)
print(f'NOMOR POLISI: {Nopol}')
print(f'TOTAL HARGA: {Total}')
print('=' * 50)
print('TERIMA KASIH')
#Selesai