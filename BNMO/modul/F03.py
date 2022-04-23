
from modul.pecah import * # manggil semua function yang ada di file matriks
from modul.cipher import*

def login(datauser):
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")
    banyak_baris = length(datauser)
    login_success = False
    while(not login_success):
        for i in range(1, banyak_baris):
            if datauser[i][1] == username and  reverse_ciphered(datauser[i][3]) == password:
                login_success = True
                user_id = datauser[i][0]
                role = datauser[i][4]
                break
        if not login_success:
            print("Password atau username salah atau tidak ditemukan")
            username = input ("Masukkan username : ")
            password = input ("Masukkan password : ")

    print("Halo " + username + "! Selamat datang di Binomo")
    return [user_id, role]
