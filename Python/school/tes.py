#mulai
L = 0
P = 0
Jumlah_Semua_Siswa = 0
Nama = ""

while Nama != "reno":
    Nama = input("Masukkan Nama Anda : ").lower()
    if Nama == "reno":
        te = " "
    else:
        Jenis_Kelamin = input("Masukkan Jenis Kelamin Anda (L/P) : ").lower()
        
    if Jenis_Kelamin == "l":
            L += 1
    elif Jenis_Kelamin == "p":
            P += 1
    else:
            te = " "
            
print("Nama Anda Adalah :", Nama)
print("Jumlah Siswa Laki-Laki :", L)
print("Jumlah Siswa Perempuan :", P)
print("-" * 30)

print("Jumlah Semua Siswa :", L + P)
#selesai