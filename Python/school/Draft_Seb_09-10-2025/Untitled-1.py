print("menu mbg pada program dasjur kelas x rpl 4")
hari_libur_diwa=input("hari libur diwa (y/t):").lower()
if hari_libur_diwa=="y":
    menu_mbg="tidak ada"
else:
        minggu=input("minggu ke:").lower()
        hari=input("hari:")
        if minggu =="1":
            if hari =="senin":
                 menu_mbg="nasi ayam goreng"
            else:
                 menu_mbg="nasi telor  orak arik"
        elif minggu=="2":
           if hari=="senin":
               menu_mbg="Nasi telor pindag"
           else:
                menu_mbg="burger chiken katsu"
        elif minggu=="3":
                if hari=="senin":
                    menu_mbg="nasi kuning tempe orek"
                else:
                    menu_mbg="nasi ayam teriyaki" 
        else:
            if hari=="senin":
             menu_mbg="roti burger chiken"
            else:
             menu_mbg="nasi liwet ayam lengkuas"
print("menu mbg")
print(menu_mbg)