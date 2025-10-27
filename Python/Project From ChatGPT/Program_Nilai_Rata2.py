print('=' * 40)
print('Program Menghitung Nilai Rata-Rata')

jumlah_nilai = 0 
Nilai_Total = 0

while True:
    # Loop internal untuk memastikan input valid
    while True:
        try:
            print('=' * 40)
            nilai_input = input('Masukkan Nilai (0-100): ')
            Nilai = int(nilai_input)
            
            if 0 <= Nilai <= 100:
                # Jika nilai valid, keluar dari loop internal
                break 
            else:
                print('=' * 40)
                print('Nilai harus di antara 0 dan 100.')
        except ValueError:
            print('=' * 40)
            print('Input tidak valid. Masukkan angka, bukan huruf.')
            # Loop akan berlanjut karena input tidak valid

    # Setelah mendapatkan nilai yang valid, tambahkan ke total
    Nilai_Total += Nilai
    jumlah_nilai += 1

    print('=' * 40)
    ulangi = input('Ulangi? (y/t): ').lower()
    if ulangi == 't':
        break

if jumlah_nilai > 0:
    Nilai_Rata_Rata = Nilai_Total / jumlah_nilai
    print('=' * 40)
    print(f'Nilai Rata-Rata Adalah: {Nilai_Rata_Rata:.2f}')
else:
    print('=' * 40)
    print('Tidak ada nilai yang dimasukkan untuk dihitung.')
