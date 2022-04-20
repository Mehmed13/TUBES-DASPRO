from modul.pecah import *
import datetime

def buy_game(datakepemilikan, datauser, datagame, datariwayat, user_id, game_id):
    banyak_baris = length(datakepemilikan)

    # cek apakah game tsb telah dimiliki oleh user
    game_owned = False
    for i in range(banyak_baris):
        if (datakepemilikan[i][0] == game_id) and (datakepemilikan[i][1] == user_id):
            game_owned = True
            break
    
    if game_owned:
        banyak_baris = length(datauser)
        banyak_kolom = hitung_kolom(datauser)

        # inisialisasi matriks data username yang sesuai dengan masukan (username yang mau beli game)
        datauser_beli = [["d" for i in range(banyak_kolom)] for j in range(2)]

        # ambil data user yang usernamenya sesuai dengan input
        indeksuser = 1
        for i in range(banyak_baris):
            datauser_beli[0] = datauser[0] # header
            if datauser[i][0] == user_id:
                datauser_beli[indeksuser] = datauser[i]
                indeksuser+=1
        
        saldouser = int(datauser_beli[1][0]) # saldo yang dimiliki oleh user

        # cari game yang sesuai dengan game_id
        banyak_baris = length(datagame)
        banyak_kolom = hitung_kolom(datagame)

         # inisialisasi matriks data username yang sesuai dengan masukan (username yang mau beli game)
        datagame_beli = [["d" for i in range(banyak_kolom)] for j in range(2)]

        # ambil data game yang sesuai
        indeksgame = 1
        for i in range(banyak_baris):
            datagame_beli[0] = datagame[0] # header
            if datagame[i][0] == game_id:
                datagame_beli[indeksgame] = datauser[i]
                indeksgame+=1
        
        namagame = datagame_beli[1][1]
        hargagame = int(datagame_beli[1][2])
        stokgame = int(datagame_beli[1][5])
        if stokgame > 0:
            if saldouser >= hargagame:
                saldobaru = saldouser - hargagame
                datauser[indeksuser][5] = str(saldobaru)
                stokgamebaru = stokgame - 1
                datagame[indeksgame][5] = str(stokgamebaru)

                # update kepemilikan
                banyak_baris = length(datakepemilikan)
                datakepemilikan[banyak_baris][0] = game_id + ";"
                datakepemilikan[banyak_baris][1] = user_id

                # update riwayat
                banyak_baris = length(datariwayat)
                datariwayat[banyak_baris][0] = game_id + ";"
                datariwayat[banyak_baris][1] = namagame + ";"
                datariwayat[banyak_baris][2] = hargagame + ";"
                datariwayat[banyak_baris][3] = user_id + ";"
                now = datetime.datetime.now()
                year = '{:02d}'.format(now.year)
                datariwayat[banyak_baris][4] = year

                print(f"Game {namagame} berhasil dibeli!")
            else:
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
        else: # stok_game = 0
            print("Stok Game tersebut sedang habis!")
    else:
        print("Anda sudah memiliki Game tersebut!")

