#PEMBUKA
print('=' * 30)
print('PROGRAM ANGKA GANJIL') 
print('=' * 30)

#INPUT
Jumlah = int(input('Masukkan Jumlah Angka Ganjil:\n'))

#PROSES DAN OUTPUT
print('=' * 30)
print('Angka ganjil:')
for i in range(Jumlah):
    angka_ganjil = 2 * i + 1
    print(angka_ganjil)
print('=' * 30)