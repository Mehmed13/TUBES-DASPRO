from matriks import *

datauser = load("users.csv")


username = input("Masukkan username : ")
password = input("Masukkan password : ")
banyak_baris = hitung_baris(datauser)

login_success = False
while(not login_success):
    for i in range(banyak_baris):
        if datauser[i][1] == username and datauser[i][3]:
            login_success = True
            name = username
            pw = password
            break
    if not login_success:
        print("Password atau username salah atau tidak ditemukan")
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")


print("Halo " + name + "! Selamat datang di “Binomo”")

# baca sambil cari -> list yang bakal menampung data user -> pas ketemu - > data di baris yang ketemu dijadiin list dan dioper ke yang lain2
