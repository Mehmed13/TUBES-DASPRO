from unicodedata import name
from modul.pecah import * 

def login(datauser):
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")
    banyak_baris = length(datauser)
    login_success = False
    while(not login_success):
        for i in range(1, banyak_baris):
            if datauser[i][1] == username and datauser[i][3] == password:
                login_success = True
                user_id = datauser[i][0]
                user_role = datauser[i][4]
                break
        if not login_success:
            print("Password atau username salah atau tidak ditemukan")
            username = input ("Masukkan username : ")
            password = input ("Masukkan password : ")

    print("Halo " + username + "! Selamat datang di Binomo")
    return user_id, user_role
