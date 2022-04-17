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
    args = parser.parse_args()
    if args.foldername == "":
        print("Tidak ada nama folder yang diberikan!")
    else:    
        if isFolderExist(args.foldername):
            datagameUTAMA = csv_to_matrix(args.foldername,"game.csv")
            datakepemilikanUTAMA = csv_to_matrix(args.foldername, "kepemilikan.csv")
            datauserUTAMA = csv_to_matrix(args.foldername, "user.csv")
            datariwayatUTAMA = csv_to_matrix(args.foldername, "riwayat.csv")
            end = False

            #login dulu
            user_id = login(datauserUTAMA)

            #Masuk Toko
            cmd = input(">>> Masukkan Command: ")

            while not end:
                if (cmd == "tambah_game"):
                    datagameUTAMA = tambah_game(datagameUTAMA)
                    cmd = input(">>> Masukkan Command: ")
                elif (cmd == "ubah_game"):
                    datagameUTAMA = ubah_game(datagameUTAMA)
                    print("")
                    cmd = input(">>> Masukkan Command: ")
                elif (cmd == "ubah_stok"):
                    datagameUTAMA = ubah_stok(datagameUTAMA)
                    print("")
                    cmd = input(">>> Masukkan Command: ")
                elif (cmd == "list_game"):
                    list_game(datagameUTAMA,datakepemilikanUTAMA,user_id)
                    print("")
                    cmd = input(">>> Masukkan Command: ")
                else:
                    end = True
        else:
            print(f'Folder "{args.foldername}" tidak ditemukan.')
print(datagameUTAMA)