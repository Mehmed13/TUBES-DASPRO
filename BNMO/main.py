from modul.pecah import *
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
from modul.F16 import *
from modul.tictactoe import *
import argparse

#ALGORIMA MAIN
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("foldername",type=str)
    try:
        args = parser.parse_args()
        if checkFolder(args.foldername):
            datagameUTAMA = csv_to_matrix(args.foldername,"game.csv")
            datakepemilikanUTAMA = csv_to_matrix(args.foldername, "kepemilikan.csv")
            datauserUTAMA = csv_to_matrix(args.foldername, "user.csv")
            datariwayatUTAMA = csv_to_matrix(args.foldername, "riwayat.csv")
            end = False

            #login dulu
            user_id, role = login(datauserUTAMA)

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
                else:
                    end = True
            print("Terimakasih telah berkunjung ke BNMO!")
        else:
            print(f'Folder "{args.foldername}" tidak ditemukan.')
    except:
        print("Tidak ada nama folder yang diberikan!")
