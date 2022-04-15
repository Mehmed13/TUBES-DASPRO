
from splitlines import *


def readFile(file, username, password):
    with open(file, "r+") as f:
        lines = f.read()
        lines = pecah(lines, "\n")
        for word in lines:
            x = pecah(word, ";")
            if username == x[1] and password == x[2]:
                return x[0], True

    return "", False


username = input("Masukkan username : ")
password = input("Masukkan password : ")

name, result = readFile("users.csv", username, password)
if result == False:
    print("Password atau username salah atau tidak ditemukan.")
else:
    print("Halo " + name + "! Selamat datang di “Binomo”")

# baca sambil cari -> list yang bakal menampung data user -> pas ketemu - > data di baris yang ketemu dijadiin list dan dioper ke yang lain2
