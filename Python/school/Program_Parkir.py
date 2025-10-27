#Mulai
print("=" * 50)
print("PROGRAM PARKIR")
print("=" * 50)

#Input
while True:
    try:
        Jenis_Kendaraan = int(input('PILIH JENIS KENDARAAN \n' \
        '1. MOTOR \n' \
        '2. MOBIL \n' \
        '3. TRUK \n'  \
        'MASUKKAN PILIHAN ANDA (1/2/3): '))
        if Jenis_Kendaraan == 1 or Jenis_Kendaraan == 2 or Jenis_Kendaraan == 3:
            break
        else:
            print('=' * 50)
            print('MASUKKAN ANGKA YANG ADA DI LIST')
            print('=' * 50)
    except ValueError:
        print('=' * 50)
        print('MASUKKAN ANGKA SAJA')
        print('=' * 50)

#Seleksi
if Jenis_Kendaraan == 1:
    Harga_Awal = 3000
    Harga_Berikutnya = 2000
elif Jenis_Kendaraan == 2:
    Harga_Awal = 5000
    Harga_Berikutnya = 3000
else:
    Harga_Awal = 8000
    Harga_Berikutnya = 5000
    
#Output
print('=' * 50)
print('HARGA PARKIR')
print(f'JAM PERTAMA: {Harga_Awal}')
print(f'JAM BERIKUTNYA: {Harga_Berikutnya}')
print('=' * 50)