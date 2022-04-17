from modul.pecah import *

#MENGUBAH STOK PADA TOKO GAME
def ubah_stok(datagameUTAMA):
    global datagameubahstok
    datagameubahstok = datagameUTAMA
    found = False

    GameIDUbah = str(input("Masukkan ID game: "))
    #Memastikan ID Game Terisi
    while (GameIDUbah == ""):
        print("")
        print("ID Game harus dimasukkan agar dapat mengubah data!") 
        GameIDUbah = str(input("Masukkan ID game: "))
    #Validasi ID Game
    for i in range (length(datagameubahstok)):
        if (datagameubahstok[i][0] == GameIDUbah):
            found = True
    if (found == False):
        print("")
        print("Tidak ada game dengan ID tersebut!")

    #Menerima Jumlah Penambahan atau Pengurangan Stok
    if (found == True):
        StokUbah = str(input("Masukkan jumlah: "))
        for i in range (length(datagameubahstok)):
            if (datagameubahstok[i][0] == GameIDUbah):
                if (StokUbah == "") or (StokUbah == "0"):
                    print("Stok game", datagameubahstok[i][1], "tidak berubah. Stok sekarang:", datagameubahstok[i][5])
                elif (int(StokUbah) < 0):
                    if (int(datagameubahstok[i][5])+int(StokUbah) < 0):
                        print("Stok game", datagameubahstok[i][1], "gagal dikurangi karena stok kurang. Stok sekarang:", datagameubahstok[i][5], "(<", str(abs(int(StokUbah)))+")")
                    else:
                        print("Stok game", datagameubahstok[i][1], "berhasil dikurangi. Stok sekarang:", int(datagameubahstok[i][5])+int(StokUbah))
                        datagameubahstok[i][5] = str(int(datagameubahstok[i][5]) + int(StokUbah))
                else:
                    print("Stok game", datagameubahstok[i][1], "berhasil ditambahkan. Stok sekarang:", int(datagameubahstok[i][5])+int(StokUbah))
                    datagameubahstok[i][5] = str(int(datagameubahstok[i][5]) + int(StokUbah))

    return datagameubahstok