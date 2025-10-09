#mulai
L = 0
P = 0
Jumlah_Semua_Siswa = 0
while True:
    Nama = input("Masukkan Nama Anda : ").lower()
    Jenis_Kelamin = input("Masukkan Jenis Kelamin Anda (L/P) : ").lower()
    if Jenis_Kelamin == "l":
        L += 1
        print("Nama Anda Adalah : ", Nama)
        print("Jumlah Siswa Laki-Laki : ", L, "\nJumlah Siswa Perempuan : ", P)
    else:
        P += 1
        print("Nama Anda Adalah : ", Nama)
        print("Jumlah Siswa Laki-Laki : ", L, "\nJumlah Siswa Perempuan : ", P)
    if Nama == "reno":
        print("Nama Anda Adalah : ", Nama
              , "\nJumlah Siswa Laki-Laki : ", L, "\nJumlah Siswa Perempuan : ", P)
        break
Jumlah_Semua_Siswa = L + P
print("Jumlah Semua Siswa Adalah : ", Jumlah_Semua_Siswa)
#selesai

