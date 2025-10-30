# Mulai
print("=" * 40)
print("          PROGRAM PARKIR")
print("=" * 40)

# Input
print("Jenis Kendaraan:")
print("1. Motor")
print("2. Mobil")
jenis = int(input("Masukkan pilihan anda (1/2)               : ")) 
nopol = input("Masukkan Nomor Polisi (Contoh: B 7543 KZZ): ").upper()
tgl_masuk = int(input("Masukkan Tanggal Masuk (1-30)             : "))
tgl_keluar = int(input("Masukkan Tanggal Keluar (1-30)            : "))
jam_masuk = int(input("Masukkan Jam Masuk (0-23)                 : "))
jam_keluar = int(input("Masukkan Jam Keluar (0-23)                : "))

# Seleksi 
if jenis == 1:  # Motor
    harga_per_jam = 3000
    jenis_kendaraan = "Motor"
else:           # Mobil
    harga_per_jam = 5000
    jenis_kendaraan = "Mobil"

# Proses 
if tgl_masuk > tgl_keluar:
    total_hari = 30 - tgl_masuk + tgl_keluar
else:
    total_hari = tgl_keluar - tgl_masuk
if jam_keluar >= jam_masuk:
    total_jam = jam_keluar - jam_masuk
else:
    total_jam = 24 - jam_masuk + jam_keluar
    total_hari -= 1
harga_hari = total_hari * 24 * harga_per_jam
harga_jam = total_jam * harga_per_jam
total_harga = harga_hari + harga_jam
lama_hari = total_hari
lama_jam = total_jam

# Output
print("\n" + "=" * 40)
print("          RINCIAN PARKIR")
print("=" * 40)
print(f"Nomor Polisi     : {nopol}")
print(f"Jenis Kendaraan  : {jenis_kendaraan}")
print(f"Biaya Parkir     : Rp{harga_per_jam:,}")
print(f"Lama Parkir      : {lama_hari} Hari dan {lama_jam} Jam")
print(f"Total Biaya      : Rp{total_harga:,}")
print("=" * 40)
print("Program Selesai")
# Selesai