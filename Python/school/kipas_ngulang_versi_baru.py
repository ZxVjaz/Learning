#MULAI
#PERULANGAN
def PERULANGAN():
    print('=== PROGRAM KIPAS ===')
    #INPUT 
    ARUS_LISTRIK = input('ADA ARUS LISTRIK (y/t): ').lower()
    if ARUS_LISTRIK == 'y':
        PUTARAN_KIPAS = input('ADA PUTARAN KIPAS (y/t): ').lower()
        if PUTARAN_KIPAS == 'y':
            ANGIN = input('ADA ANGIN (y/t): ').lower()
            print('-' * 40) #PEMBATAS
            if ANGIN == 'y':
                print('KIPAS BERFUNGSI DAN ANGINNYA MERATA')
            else:
                print('KIPAS BERFUNGSI DAN ANGINNYA TIDAK MERATA')
        else:
            print('-' * 40) #PEMBATAS
            print('⚠️  WARNING ⚠️ KIPAS TIDAK BERFUNGSI')
    else:
        print('-' * 40) #PEMBATAS
        print('⚠️  WARNING ⚠️ KIPAS TIDAK BERFUNGSI')
    
    print('-' * 40) #PEMBATAS
    ULANGI = input('ULANGI? (y/t): ').lower()
    if ULANGI == 'y':
        return PERULANGAN()
    else:
        return

PERULANGAN()
#SELESAI