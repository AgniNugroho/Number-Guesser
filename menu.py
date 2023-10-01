import core
import os
import time as t

def end():
    print('\n1. Main Lagi\n2. Keluar\n3. Menu Utama')
    inp = int(input('> '))
    if inp == 1:
        core.diff()
    if inp == 2:
        exit()
    if inp == 3:
        mainmenu()
    else:
        print('Input tidak valid!')
        t.sleep(1.9)
        os.system('cls')
        end()

def exit():
    os.system('cls')

def help():
    os.system('cls')
    print('Dalam permainan ini, kamu harus menebak angaka acak antara 0-20 (kecuali kustom).\nJika muncul tanda ⬆️ artinya angka jawaban bernilai lebih tinggi dari angka yang anda tebak dan begitu juga sebalilnya.\nSELAMAT BERMAIN')
    helpmenu()

def mainmenu():
    os.system('cls')
    print('Number Guesser'.center(24,' '))
    print('v 1.3'.center(24,' '))
    print('By Agni Nugroho'.center(24,' '))
    print(f'\n1. Main\n2. Bantuan\n3. Pengaturan\n4. Keluar\n\n')
    menu = int(input('> '))
    if menu == 1:
        core.diff()
    if menu == 2:
        help()
    if menu == 3:
        options()
    if menu == 4:
        exit()
    else:
        print('Input tidak valid!')
        t.sleep(1.9)
        mainmenu()

def helpmenu():
    print('\n1. Menu Utama\n2. Main\n3. Keluar')
    hp = int(input('> '))
    if hp == 1:
        mainmenu()
    if hp == 2:
        core.diff()
    if hp == 3:
        exit()
    else:
        print('Input tidak valid!')
        t.sleep(1.9)
        os.system('cls')
        help()
        helpmenu()

def options():
    os.system('cls')
    print('Pengaturan'.center(24,' '))
    print('\n1. Warna Font & Background\n9. Menu Utama')
    inp = int(input('> '))
    if inp == 1:
        fontcolor()
    if inp == 9:
        mainmenu()
    else:
        print('Input tidak valid!')
        t.sleep(1.9)
        os.system('cls')
        options()

def fontcolor():
    os.system('cls')
    print('Warna Font & Background'.center(24,' '))
    print('\n0.Hitam\n1. Biru\n2. Hijau\n3. Biru Muda\n4. Merah\n5. Ungu\n6. Oranye\n7. Putih\n8. Abu-abu')
    print('\nMasukkan Warna Font')
    fnt = int(input('> '))
    os.system('cls')
    print('Warna Font & Background'.center(24,' '))
    print('\n0.Hitam\n1. Biru\n2. Hijau\n3. Biru Muda\n4. Merah\n5. Ungu\n6. Oranye\n7. Putih\n8. Abu-abu')
    print('\nMasukkan Warna Background')
    bg = int(input('> '))
    os.system(f'color {bg}{fnt}')
    options()