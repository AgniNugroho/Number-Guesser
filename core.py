import random as r
import os
import menu

def play():
    os.system('cls')
    a = r.randrange(0,20)
    chance = 10
    print('0-20')
    for i in range(chance):
        print(f'Sisa {chance} kesempatan.')
        i = int(input('> '))
        if i > a:
            print('⬇️')
            chance -= 1
        elif i < a:
            print('⬆️')
            chance -= 1
        elif i == a:
            print(f'Kamu Menang!!!\nJawabannya adalah {a}')
            break
        if chance == 0:
            print(f'Kesempatanmu Habis. Jawabannya adalah {a}\nSemoga Beruntung Lain Kali.')
            break
    menu.end()

def playhard():
    os.system('cls')
    a = r.randrange(0,20)
    chance = 5
    print('0-20')
    for i in range(chance):
        print(f'Sisa {chance} kesempatan.')
        i = int(input('> '))
        if i > a:
            print('⬇️')
            chance -= 1
        elif i < a:
            print('⬆️')
            chance -= 1
        elif i == a:
            print(f'Kamu Menang!!!\nJawabannya adalah {a}')
            break
        if chance == 0:
            print(f'Kesempatanmu Habis. Jawabannya adalah {a}\nSemoga Beruntung Lain Kali.')
            break
    menu.end()

def custom():
    os.system('cls')
    print('Masukkan Batas Bawah')
    bb = int(input('> '))
    os.system('cls')
    print('Masukkan Batas Atas')
    ba = int(input('> '))
    os.system('cls')
    a = r.randrange(bb,ba)
    print('Masukkan Kesempatan')
    chance = int(input('> '))
    os.system('cls')
    print(f'{bb}-{ba}')
    for i in range(chance):
        print(f'Sisa {chance} kesempatan.')
        i = int(input('> '))
        if i > a:
            print('⬇️')
            chance -= 1
        elif i < a:
            print('⬆️')
            chance -= 1
        elif i == a:
            print(f'\nKamu Menang!!!\nJawabannya adalah {a}')
            break
        if chance == 0:
            print(f'\nKesempatanmu Habis. Jawabannya adalah {a}.\nSemoga Beruntung Lain Kali.')
            break
    menu.end()

def diff():
    os.system('cls')
    print('Mode Permainan\n\n1. Mudah (10 Kesempatan)\n2. Sulit (5 Kesempatan)\n3. Kustom')
    d = int(input('> '))
    if d == 1:
        play()
    if d == 2:
        playhard()
    if d == 3:
        custom()    