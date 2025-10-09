print('Menu MBG pel. Dasjur X RPL 4')
weekend = input('Hari Libur (y/t)? \n').lower()
week = input('minggu ke (1-4)? \n')
day = input('hari (senin/kamis)? \n').lower()
if weekend == 'y':
    menu_mbg = 'tidak ada mbg, hari libur'
else:
    if week == '1':
        if day == 'senin':
            menu_mbg = 'nasi ayam goreng'
        else:
            menu_mbg = 'nasi telur orak arik'
    elif week == '2':
        if day == 'senin':
            menu_mbg = 'nasi telur pindang'
        else:
            menu_mbg = 'burger chicken katsu'
    elif week == '3':
        if day == 'senin':
            menu_mbg = 'nasi kuning tempe orek'
        else:
            menu_mbg = 'nasi ayam teriyaki'
    else:
        if day == 'senin':
            menu_mbg = 'roti burger chicken katsu'
        else:
            menu_mbg = 'nasi liwet ayam lengkuas'
print('menu mbg')
print(menu_mbg)