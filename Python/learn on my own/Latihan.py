# FILE: game_sederhana.py

# 1. VARIABLE (Tempat nyimpen data)
nyawa = 100
uang = 50

# 2. FUNGSI-FUNGSI (Cara main game)
def tampilkan_status():
    print(f"Nyawa: {nyawa}")
    print(f"Uang: {uang}")

def mulai_perang():
    print("⚔️ PERANG DIMULAI!")
    print("Kamu menang! Dapat 10 uang!")
    return 10  # balikin uang yang didapat

def toko():
    print("🏪 SELAMAT DATANG DI TOKO")
    print("Kamu beli potion -5 uang")
    return -5  # uang berkurang

# 3. MENU UTAMA
def menu_utama():
    print("\n=== GAME SEDERHANA ===")
    tampilkan_status()
    
    print("\nPilihan:")
    print("1. Mulai perang")
    print("2. Pergi ke toko") 
    print("3. Keluar")
    
    pilihan = input("Pilih 1-3: ")
    
    if pilihan == "1":
        uang_tambahan = mulai_perang()
        global uang
        uang += uang_tambahan
    elif pilihan == "2":
        uang_berkurang = toko() 
        uang += uang_berkurang
    elif pilihan == "3":
        print("Dadah!")
        return False  # berhenti game
    else:
        print("Pilihan salah!")
    
    return True  # lanjut game

# 4. 🎮 INI YANG BIKIN GAME JALAN!
print("🎮 GAME DIMULAI! 🎮")
print("Selamat datang!")

# Game loop - biar game jalan terus
game_berjalan = True
while game_berjalan:
    game_berjalan = menu_utama()

print("🎮 GAME SELESAI! 🎮")