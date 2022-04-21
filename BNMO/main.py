from modul.F02 import *
from modul.F03 import *
from modul.F04 import *
from modul.F05 import *
from modul.F06 import *
from modul.F07 import *
from modul.F08 import *
from modul.F09 import *
from modul.F10 import *
from modul.F11 import *
from modul.F12 import *
from modul.F13 import *
from modul.F14 import *
from modul.F15 import *
from modul.F16 import *
from modul.F17 import *
from modul.pecah import *
from modul.tictactoe import *
from modul.kerangajaib import *


import argparse

#ALGORIMA MAIN
if __name__ == "__main__":
    
    load_dir = load()
    if load_dir != "":
        datagameUTAMA = csv_to_matrix(load_dir,"game.csv")            
        datakepemilikanUTAMA = csv_to_matrix(load_dir, "kepemilikan.csv")
        datauserUTAMA = csv_to_matrix(load_dir, "user.csv")
        datariwayatUTAMA = csv_to_matrix(load_dir, "riwayat.csv")
        end = False
        login_success = False
        #login dulu
        while not login_success:
            cmd = input(">>> Masukkan Command: ")
            if cmd != "login":
                print('Maaf, Anda harus login terlebih dahulu untuk memberi command selain "login"')
            else:
                user_id, role = login(datauserUTAMA)
                login_success = True
        #register


        #Masuk Toko
        cmd = input(">>> Masukkan Command: ")

        while not end:
            if (cmd == "tambah_game"):
                if (role == "admin"):
                    datagameUTAMA = tambah_game(datagameUTAMA)
                else:
                    print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                cmd = input(">>> Masukkan Command: ")
            elif (cmd == "ubah_game"):
                if (role == "admin"):
                    datagameUTAMA = ubah_game(datagameUTAMA)
                else:
                    print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                print()
                cmd = input(">>> Masukkan Command: ")                       
            elif (cmd == "ubah_stok"):
                if (role == "admin"):
                    datagameUTAMA = ubah_stok(datagameUTAMA)
                else:
                    print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                print()
                cmd = input(">>> Masukkan Command: ")
            elif (cmd == "list_game"):
                if (role == "user"):
                    list_game(datagameUTAMA,datakepemilikanUTAMA,user_id)
                else:
                    print("Maaf Anda harus menjadi user untuk melakukan hal tersebut.")
                print()
                cmd = input(">>> Masukkan Command: ")
            elif (cmd == "list_game_toko"):
                list_game_toko(datagameUTAMA)
                print()
                cmd = input(">>> Masukkan Command: ")
            elif (cmd == "search_my_game"):
                if (role == "user"):
                    search_my_game(datakepemilikanUTAMA, datagameUTAMA,user_id)
                else:
                    print("Maaf Anda harus menjadi user untuk melakukan hal tersebut.")
                print()
                cmd = input(">>> Masukkan Command: ")
            elif (cmd=="search_game_at_store"):
                search_game_at_store(datagameUTAMA)
                print()
                cmd = input(">>> Masukkan Command: ")
            elif (cmd == "buy_game"):
                if (role == "user"):
                    databuy =buy_game(datakepemilikanUTAMA,datauserUTAMA,datagameUTAMA,datariwayatUTAMA, user_id)
                    #penyimpanan pengubahan data sementara pada matriks data
                    datakepemilikanUTAMA = databuy[0]
                    datauserUTAMA= databuy[1]
                    datagameUTAMA = databuy[2]
                    datariwayatUTAMA = databuy[3]
                else:
                    print("Maaf Anda harus menjadi user untuk melakukan hal tersebut.")
                print()
                cmd = input(">>> Masukkan Command: ")
            elif(cmd == "riwayat"):
                if (role == "user"):
                    riwayat(datariwayatUTAMA,user_id)
                else:
                    print("Maaf Anda harus menjadi user untuk melakukan hal tersebut.")
                print()
                cmd = input(">>> Masukkan Command: ")
            elif (cmd == "topup"):
                if (role == "admin"):
                    datauserUTAMA =  topup(datauserUTAMA)
                else:
                    print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                print()
                cmd = input(">>> Masukkan Command: ")
            elif(cmd == "tictactoe"):
                tictactoe()
                print()
                cmd = input(">>> Masukkan Command: ")
            elif(cmd == "kerangajaib"):
                kerangajaib()
                print()
                cmd = input(">>> Masukkan Command: ")
            elif(cmd == "exit"):
                func_exit(datagameUTAMA, datakepemilikanUTAMA, datariwayatUTAMA, datauserUTAMA)
            elif(cmd == "register"):
                if (role == "admin"):
                    register(datauserUTAMA)
                else:
                    print("Maaf kamu tidak memiliki izin untuk menjalankan perintah berikut")
                cmd = input(">>> Masukkan Command: ")
            elif(cmd == "save"):
                save(datagameUTAMA, datakepemilikanUTAMA, datariwayatUTAMA, datauserUTAMA)
                cmd = input(">>> Masukkan Command:")
            else:
                print("Maaf command yang anda masukkan tidak tersedia pada aplikasi BNMO!")
                cmd = input(">>> Masukkan Command: ")
        print("Terima kasih telah berkunjung ke BNMO!")
    else:
        print("Maaf, setup tidak sesuai.")

