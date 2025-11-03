# Start
print('=' * 75)
print('		PROGRAM MENENTUKAN PERMAINAN DI PASAR MALAM')
print('=' * 75)

# Input
nama = str(input('\nMASUKKAN NAMA		:'))
usia = int(input('MASUKKAN USIA	  	:'))
jenisKelamin = str(input('JENIS KELAMIN (L/P)	:')).upper()

# Seleksi
if usia >= 6 and usia <= 12:
    if jenisKelamin == 'L':
        permainan = str('Bianglala, Komedi Putar, Rumah Hantu')
    elif jenisKelamin == 'P':
        permainan = str('Bianglala, Komedi Putar, Ombak Banyu')
elif usia >= 13 and usia <= 17:
    if jenisKelamin == 'L':
        permainan = str('Bianglala, Komedi Putar, Rumah Hantu, Kora-Kora')
    elif jenisKelamin == 'P':
        permainan = str('Bianglala, Komedi Putar, Rumah Hantu')
else:
    permainan = str('Kriteria tidak memenuhi permainan apapun')
    
if jenisKelamin == 'L':
    jenisKelamin = 'Laki-Laki'
elif jenisKelamin == 'P':
    jenisKelamin = 'Perempuan'
else:
    jenisKelamin = 'Tidak diketahui'
        
# Output
print('=' * 75)
print('hasil')
print(f'Anda yang bernama {nama} Jenis Kelamin {jenisKelamin} Usia anda {usia}\n' \
        f'tahun lahir anda adalah {2025 - usia}\n' \
        f'Permainan yang boleh diambil {permainan}')
# Stop
