# Jangan lupa untuk set file ini menjadi tersembunyi!

import os
import time as t

def password():
    database = {
        'NobFrostt':'P0314003101778'
    }

    os.system('cls')
    user = input('Username: ')
    passwd = input('Password: ')
    a = database.get(user)
    while a != passwd:
        while a == None:
            print(f'{user} is not in our databese. Please try again! ')
            t.sleep(1.9)
            os.system('cls')
            user = input('Username: ')
            passwd = input('Password: ')
            a = database.get(user)
        if a == passwd:
            break
        print(f'Incorrect password for {user}, Please try again!')
        t.sleep(1.9)
        os.system('cls')
        user = input('Username: ')
        passwd = input('Password: ')
        a = database.get(user)
    print('Welcome')