#PEMBUKAAN
print('=' * 30)
print('  PROGRAM BILANGAN PRIMA')
print('=' * 30)

#INPUT
Jumlah = int(input('Masukkan Jumlah Bilangan Prima:\n'))

#PROSES DAN OUTPUT
print('=' * 30)
print('Bilangan prima:')
o = 0
num = 2  
while o < Jumlah:
    is_prima = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prima = False
            break
    if is_prima:
        print(num)
        o += 1  
    num += 1  

print('=' * 30)