from modul.pecah import *

def topup(datauser):
    username = input("Masukkan username: ")
    topup = int(input("Masukkan saldo: "))
    banyak_baris = length(datauser)
    user_exist = False
    # ambil data user yang usernamenya sesuai dengan input

    for i in range(banyak_baris):
        if datauser[i][1] == username:
            datauser_topup = datauser[i]
            user_exist = True
            indeks_user = i
            break    

    # jika tidak ditemukan username yang sesuai, maka baris kedua hanya berisi "d"
    if not user_exist:
        print("Username "" + username + "" tidak ditemukan.")
    else: # jika username ada, proceed top-up
        saldo = int(datauser_topup[5])
        saldo += topup #penambahan saldo
        if saldo < 0:
            print("Masukan tidak valid.")
        else: # saldo yang baru >= 0, top-up berhasil
            datauser_topup[5] = str(saldo)
            print(f"Top up berhasil. Saldo {username} bertambah menjadi {saldo}.")
    #modif data
    datauser[indeks_user] = datauser_topup
    return datauser
