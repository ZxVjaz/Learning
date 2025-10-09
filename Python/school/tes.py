#mulai
L = 0
P = 0
Nama = ""

while Nama != "reno":
    Nama = input("Masukkan Nama Anda : ").lower()
    
    if Nama != "reno":
        Jenis_Kelamin = input("Masukkan Jenis Kelamin Anda (L/P) : ").lower()
        
        if Jenis_Kelamin == "l":
            L += 1
            print("Jumlah Siswa Laki-Laki :", L)
            print("Jumlah Siswa Perempuan :", P)
        elif Jenis_Kelamin == "p":
            P += 1
            print("Jumlah Siswa Laki-Laki :", L)
            print("Jumlah Siswa Perempuan :", P)
#selesai