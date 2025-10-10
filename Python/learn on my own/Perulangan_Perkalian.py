#import library
import time

#Judul
print('=' * 30)
print(' ' * 4, "Perulangan Perkalian")
print('=' * 30)

#Deskripsi
print('program ini berfungsi untuk menampilkan proses perkalian satu-persatu')

#Input
num1 = int(input('Masukkan angka pertama: '))
num2 = int(input('Masukkan angka kedua: '))

#Proses dan Output
def proses(num1, num2):
    global hasil
    hasil = 0
    for i in range(1, num2 + 1):    
        hasil = num1 * i
        time.sleep(0.25)
        print(hasil)
        
    return hasil
proses(num1, num2)

#Kesimpulan
print('=' * 30)
print(f"Kesimpulan: {num1} x {num2} = {hasil}")




