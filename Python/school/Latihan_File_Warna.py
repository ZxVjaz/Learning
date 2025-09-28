def RedoPoint(Jumlah_Warna=0):
    Warna = input('Masukan Warna=')
    Ulangi = input('Ulangi? (y/t)=')
    
    if Ulangi.lower() == 'y':
        print('Warna=', Warna)
        Jumlah_Warna = Jumlah_Warna + 1
        return RedoPoint(Jumlah_Warna)
    else:
        print('Warna=', Warna)
        Jumlah_Warna = Jumlah_Warna + 1
        return Jumlah_Warna

print("=== PROGRAM PENCATAT WARNA ===")
total = RedoPoint()
print('Jumlah Warna=', total)
print('program selesai')