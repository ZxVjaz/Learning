#MULAI
print('=== PROGRAM KIPAS ===')
#INPUT 
ARUS_LISTRIK = input('ADA ARUS LISTRIK (y/t): ').lower()
PUTARAN_KIPAS = input('ADA PUTARAN KIPAS (y/t): ').lower()
ANGIN = input('ADA ANGIN (y/t): ').lower()
#SELEKSI
if ARUS_LISTRIK  == 'y':
    if PUTARAN_KIPAS == 'y':
        if ANGIN == 'y':
            print('-' * 40)
            print('KIPAS BERFUNGSI')
        else:
             print('KIPAS TIDAK BERFUNGSI')
    else:
        print('KIPAS TIDAK BERFUNGSI')
else:
    print('KIPAS TIDAK BERFUNGSI')
END = input('\npencet tombol apapun untuk keluar....')
#SELESAI