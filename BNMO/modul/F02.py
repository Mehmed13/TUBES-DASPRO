from modul.pecah import * 
from modul.cipher import *

def register(datauser):
    nama = input("Masukkan nama user baru:")
    username= input("Masukkan username baru:")
    password= input("Masukkan password:")

    exist = False   #Perbandingan untuk mengecek apakah username sudah digunakan
    for baris in datauser:
        if (baris[1] == username): #untuk mengecek pada tiap baris di kolom [1]
            exist = True
            
    if exist != True: #jika belum ada maka akan register dan memasukkan ke dalam matriks
        data = [str(length(datauser)), username, nama, ciphered(password) , "user", "0"]
        datauser += [data]
        print("Selamat, " + username + " telah berhasil diregistrasikan.")
    else:
        print("Maaf,username  telah terpakai.")
