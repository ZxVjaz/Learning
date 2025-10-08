print("===============================")
print("=== Daftar MBG Pelajaran Dasjur ===")
print("===============================")

Hari_Libur = input("Hari Libur (y/t): ").lower()
Minggu = input("Minggu (1-4): ")
Hari = input("Hari (Senin/Kamis): ").lower()

if Hari_Libur == 'y':
    print("MBG tidak ada karena hari libur.")
else:
    if Minggu == '1':
        if Hari == 'senin':
            MBG = "Nasi uduk"    
        else:
            MBG = "Sayur Asem"
    elif Minggu == '2':
        if Hari == 'senin':
            MBG = "Nasi Goreng"
        else:
            MBG = "Soto Ayam"
    elif Minggu == '3':
        if Hari == 'senin':
            MBG = "Mie Ayam"
        else:
            MBG = "Bakso"
    else:
        if Hari == 'senin':
            MBG = "Pecel Lele"
        else:
            MBG = "Ayam Geprek"

print("Menu MBG")
print(MBG)