#MISALKAN SAJA SUDAH ADA (NANTI DIHAPUS):
user_id = "ayam123"

import pecah

#MENAMPUNG GAME ID MILIK USER TERTENTU
banyak_game = 0
for i in range(pecah.banyak_baris_kepemilikan):   
    if (pecah.datakepemilikan[i][1] == user_id):
        banyak_game = banyak_game + 1

list_gameid = ["d" for i in range(banyak_game)]
count = 0
for i in range(pecah.banyak_baris_kepemilikan):
    if (pecah.datakepemilikan[i][1] == user_id):
        list_gameid[count] = pecah.datakepemilikan[i][0]
        count = count + 1

#MELIHAT LIST GAME MILIK USER TERTENTU
def list_game():
    global lihatgame
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
            for j in range(pecah.banyak_baris):
                if (pecah.datagame[j][0] == list_gameid[i]):
                    lihatgame[daftar][1] = pecah.datagame[j][0]
                    lihatgame[daftar][2] = pecah.datagame[j][1]
                    lihatgame[daftar][3] = pecah.datagame[j][3]
                    lihatgame[daftar][4] = pecah.datagame[j][4]
                    lihatgame[daftar][5] = pecah.datagame[j][2]
                    daftar = daftar + 1
        print("Daftar Game:")
        for i in range(banyak_game):
            print(lihatgame[i][0], lihatgame[i][1], "|", lihatgame[i][2], "|", lihatgame[i][3], "|", lihatgame[i][4], "|", lihatgame[i][5])
