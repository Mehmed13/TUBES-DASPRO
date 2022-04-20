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
    banyak_kolom = length(datagame[0])
    if (banyak_game == 0):
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:
        lihatgame = [["" for i in range(banyak_kolom-1)] for j in range(banyak_game+1)]
            # Data Kolom
            #ID Game | Nama | Kategori | Tahun | Harga
        indeks_kolom = 0
        for i in range (banyak_kolom):
            if i != 5:
                lihatgame[0][indeks_kolom] = datagame[0][i] #header
                indeks_kolom += 1
        
        daftar = 1
        for i in range(1, banyak_game+1):
            for j in range(banyak_baris_game):
                if (datagame[j][0] == list_gameid[i-1]):
                    indeks_kolom = 0
                    for k in range (banyak_kolom):
                        if k != 5:
                            lihatgame[daftar][indeks_kolom]= datagame[j][k]
                            indeks_kolom += 1
                    daftar = daftar + 1
        print("Daftar Game:")
        cetakdata(lihatgame, banyak_kolom-1,banyak_game+1)
