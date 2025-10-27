#konversi detik
print('Konversi Detik')
Detik = int(input('Masukkan Detik: '))
Jam = Detik // 3600
Sisa_Detik = Detik % 3600
Menit = Sisa_Detik // 60
Detik = Sisa_Detik % 60
print(f'{Jam} Jam, {Menit} Menit, {Detik} Detik')