from F07 import *

username = input("Masukan username: ")
topup = int(input("Masukan saldo: "))

# ambil data user
baca = open("user.csv","r") 
listuser = baca.readlines()        #Penyimpanan isi file pada variabel
banyak_baris = hitung_baris(listuser)
banyak_kolom = hitung_kolom(listuser)
datauser = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)] 
datauser = pecah_csv(listuser, datauser)
# Terbentuk Data Kolom
# id | username | nama | password | role | saldo
baca.close()
# sudah terbentuk matriks user.csv

# inisialisasi matriks data username yang sesuai dengan masukan (username yang mau ditop-up)
datauser_topup = [["d" for i in range(banyak_kolom)] for j in range(2)]

# ambil data user yang usernamenya sesuai dengan input
indeks = 1
for i in range(banyak_baris):
    datauser_topup[0] = datauser[0] # header
    if datauser[i][1] == username:
        datauser_topup[indeks] = datauser[i]
        indeks+=1

# jika tidak ditemukan username yang sesuai, maka baris kedua hanya berisi "d"
if datauser_topup[1][1] == "d":
    print("Username "" + username + "" tidak ditemukan.")
else: # jika username ada, proceed top-up
    saldo = int(datauser_topup[1][5])
    saldobaru = saldo + topup
    if saldo < 0:
        print("Masukan tidak valid.")
    else: # saldo yang baru >= 0, top-up berhasil
        datauser_topup[1][5] = str(saldobaru)
        print(f"Top up berhasil. Saldo {username} bertambah menjadi {saldobaru}.")