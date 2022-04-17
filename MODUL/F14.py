import os
from F02 import *
from F03 import *

def help():
    print("Loading...")

    print('Selamat datang di antarmuka "Binomo"')

    role = input("Masukkan role : ")
    if role == "admin":
        print("============ HELP ============")
        print("1. register - Untuk melakukan registrasi user baru")
        print("2. login - Untuk melakukan login ke dalam sistem")
        print("3. tambah_game - Untuk menambah game yang dijual pada toko")
        print("4. list_game_toko - Untuk melihat list game yang dijual pada toko")
        menu = input("Masukkan menu : ")
        if menu == "1":
           register()
        elif menu == "2":
           login()
        elif menu == "3":
           os.system('python3 F02.py')
        elif menu == "4":
           os.system('python3 F02.py')
    else:
        print("============ HELP ============")
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")
        menu = input("Masukkan menu : ")
        if menu == "1":
           login()
        elif menu == "2":
           os.system('python3 F02.py')
        
if __name__ == "__main__":
    help()