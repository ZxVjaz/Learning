import ctypes
import time

def lock_and_turn_off():
    """Lock workstation lalu paksa matiin layar"""
    # Lock dulu
    ctypes.windll.user32.LockWorkStation()
    print("Workstation locked...")
    
    # Tunggu 2 detik biar lock process selesai
    time.sleep(2)
    
    # Paksa matiin layar
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x0112, 0xF170, 2)
    print("Monitor turned off!")

lock_and_turn_off()