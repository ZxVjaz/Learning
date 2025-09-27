#PEMBUKA
print('=' * 30)
print('PROGRAM ANGKA GENAP') 
print('=' * 30)

#INPUT
Jumlah = int(input('Masukkan Jumlah Angka Genap:\n'))

#PROSES DAN OUTPUT
print('=' * 30)
print('Angka Genap:')
for i in range(Jumlah):
    angka_genap = 2 * i
    print(angka_genap)
print('=' * 30)