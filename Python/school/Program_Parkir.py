#Mulai
print("=" * 50)
print("PROGRAM PARKIR")
print("=" * 50)

#Input
while True:
    try:
        Jenis_Kendaraan = int(input('PILIH JENIS KENDARAAN \n' \
        '1. Motor \n' \
        '2. Mobil \n' \
        '3. Truk \n' ))
        break
    except ValueError:
        print('=' * 50)
        print('masukkan angkanya saja')
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
print('Harga Parkir')
print(f'Jam Pertama: {Harga_Awal}')
print(f'Jam Berikutnya: {Harga_Berikutnya}')
print('=' * 50)