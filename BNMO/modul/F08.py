from modul.pecah import *
import datetime

def buy_game(datakepemilikan, datauser, datagame, datariwayat, user_id):
    #meminta game_id
    game_id = input("Masukkan ID Game: ")
    
    banyak_baris = length(datakepemilikan)

    # cek apakah game tsb telah dimiliki oleh user
    game_owned = False
    for i in range(banyak_baris):
        if (datakepemilikan[i][0] == game_id) and (datakepemilikan[i][1] == user_id):
            game_owned = True
            break
    
    if not game_owned: #Jika game belum dimiliki
        banyak_baris = length(datauser)

        # ambil data user yang user_id nya sesuai dengan input
        for i in range(banyak_baris):
            if datauser[i][0] == user_id: 
                datauser_beli = datauser[i] #hanya mungkin ada satu data untuk satu user
                indeks_user = i
                break
        
        saldouser = int(datauser_beli[5]) # saldo yang dimiliki oleh user

        # cari game yang sesuai dengan game_id
        banyak_baris = length(datagame)

        # ambil data game yang sesuai
        for i in range(banyak_baris):
            if datagame[i][0] == game_id:
                datagame_beli = datagame[i]
                indeks_game = i
                break
        
        #penyimpanan beberapa variabel transaksi
        namagame = datagame_beli[1]
        hargagame = int(datagame_beli[2])
        stokgame = int(datagame_beli[5])
        
        if stokgame > 0: #jika stok game masih ada
            if saldouser >= hargagame: #jika saldo user cukup untuk membeli game
                
                #modifikasi data game dan data user
                saldouser -= hargagame 
                datauser[indeks_user][5] = str(saldouser) 
                stokgame -= 1  
                datagame[indeks_game][5] = str(stokgame) 

                # update kepemilikan
                kepemilikan_baru = [game_id,user_id]
                datakepemilikan = append(datakepemilikan,kepemilikan_baru)

                # update riwayat
                now = datetime.datetime.now()
                year = '{:02d}'.format(now.year)
                riwayat_baru = [game_id,namagame,hargagame,user_id,year]
                datariwayat= append(datariwayat,riwayat_baru)

                print(f"Game {namagame} berhasil dibeli!")
            else: #jika saldo tak cukup
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
        else: # stok_game = 0
            print("Stok Game tersebut sedang habis!")
    else:#jika sudah memiliki game
        print("Anda sudah memiliki Game tersebut!")
    return [datakepemilikan,datauser,datagame,datariwayat]
