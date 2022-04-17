from matriks import * # manggil semua function yang ada di file matriks

def login():
    datauser = load("users.csv") # nge load file users.csv

    username = input("Masukkan username : ")
    password = input("Masukkan password : ")
    banyak_baris = hitung_baris(datauser)

    login_success = False
    while(not login_success):
        for i in range(banyak_baris):
            if datauser[i][1] == username and datauser[1][3]:
                login_success = Truename =username
                name = username
                pw = password
            if not login_success :
                print("Password atau username salah atau tidak ditemukan")
                username = input ("Masukkan username : ")
                password = input ("Masukkan password : ")

    print("Halo" + name + "! Selamat datang di Binomo")

if __name__ == "__main__":
    login()