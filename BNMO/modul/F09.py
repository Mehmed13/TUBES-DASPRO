from modul.pecah import*

#MENAMPUNG GAME ID MILIK USER TERTENTU
def gameid_user(datakepemilikan, user_id):
    global banyak_game, list_gameid
    banyak_game = 0
    banyak_baris_kepemilikan = length(datakepemilikan)
    for i in range(banyak_baris_kepemilikan):   
        if (datakepemilikan[i][1] == user_id):
            banyak_game = banyak_game + 1
    list_gameid = ["d" for i in range(banyak_game)]
    count = 0
    for i in range(banyak_baris_kepemilikan):
        if (datakepemilikan[i][1] == user_id):
            list_gameid[count] = datakepemilikan[i][0]
            count = count + 1



#MELIHAT LIST GAME MILIK USER TERTENTU
def list_game(datagame, datakepemilikan, users_id):
    global lihatgame
    gameid_user(datakepemilikan,users_id)
    banyak_baris_game = length(datagame)
    if (banyak_game == 0):
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:
        lihatgame = [["" for i in range(6)] for j in range(banyak_game)]
            # Data Kolom
            # Nomor | ID Game | Nama | Kategori | Tahun | Harga
        nomor = 1
        for i in range(banyak_game):
            lihatgame[i][0] = str(nomor)+"."
            nomor = nomor + 1

        daftar = 0
        for i in range(banyak_game):
            for j in range(banyak_baris_game):
                if (datagame[j][0] == list_gameid[i]):
                    lihatgame[daftar][1] = datagame[j][0]
                    lihatgame[daftar][2] = datagame[j][1]
                    lihatgame[daftar][3] = datagame[j][3]
                    lihatgame[daftar][4] = datagame[j][4]
                    lihatgame[daftar][5] = datagame[j][2]
                    daftar = daftar + 1
        print("Daftar Game:")
        for i in range(banyak_game):
            print(lihatgame[i][0], lihatgame[i][1], "|", lihatgame[i][2], "|", lihatgame[i][3], "|", lihatgame[i][4], "|", lihatgame[i][5])