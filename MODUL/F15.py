import argparse
from matriks import *
from F14 import *

def Load():
    syntax = argparse.ArgumentParser() # memanggil argparse
    syntax.add_argument("folder", type=str) # menambahkan argument berupa nama folder
    args = syntax.parse_args() # menampung input user ke dalam variable "args"
    folderName = args.folder # memindahkan input user ke dalam variable "folderName"
    resultCheck = checkFolder(folderName) # memanggil fungsi pengecekan folder
    if resultCheck != True: # jika folder tidak ditemukan, maka muncul perintah "Folder ... tidak ditemukan."
        print("Folder "+folderName+ " tidak ditemukan.")
    else: # jika folder udah ada
        help() # panggil function HELP (F14)

if __name__ == "__main__":
    Load()