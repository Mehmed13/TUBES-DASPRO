from F07 import *

user_id = "rendangdong" # ceritanya lagi login pakai id ini yah, soalnya yg ayam123 rolenya admin

baca = open("kepemilikan.csv","r") 
listKepemilikan = baca.readlines()        #Penyimpanan isi file pada variabel
banyak_baris = hitung_baris(listKepemilikan)
banyak_kolom = hitung_kolom(listKepemilikan)
datakepemilikan = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)] 
datakepemilikan = pecah_csv(listKepemilikan, datakepemilikan)
# Data berbentuk tabel
# game_id | user_id
baca.close()
# sudah terbentuk matriks kepemilikan.csv

game_id = input("Masukkan ID Game: ")

game_owned = False
# cek apakah game tsb telah dimiliki oleh user
for i in range(banyak_baris):
    if (datakepemilikan[i][0] == game_id) and (datakepemilikan[i][1] == user_id):
        game_owned = True
        break
print(game_owned) # MASIH FLAWED CARI GAME_OWNEDNYA!!!

# if game_owned:
if game_owned:
    baca = open("user.csv","r") 
    listuser = baca.readlines()        #Penyimpanan isi file pada variabel
    banyak_baris = hitung_baris(listuser)
    banyak_kolom = hitung_kolom(listuser)
    datauser = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)] 
    datauser = pecah_csv(listuser, datauser)
    # Terbentuk Data Kolom
    # id | username | nama | password | role | saldo
    baca.close()

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

    # cari game yang sesuai, pertama buat matriks data game
    baca = open("game.csv","r") 
    listgame = baca.readlines()        #Penyimpanan isi file pada variabel
    banyak_baris = hitung_baris(listgame)
    banyak_kolom = hitung_kolom(listgame)
    datagame = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)] 
    datagame = pecah_csv(listgame, datagame)
    # Terbentuk Data Kolom
    # ID Game | Nama Game | Harga | Kategori | Tahun Rilis | Stok
    baca.close()

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
            # update riwayat
            print(f"Game {namagame} berhasil dibeli!")
        else:
            print("Saldo anda tidak cukup untuk membeli Game tersebut!")
    else: # stok_game = 0
        print("Stok Game tersebut sedang habis!")
else:
    print("Anda sudah memiliki Game tersebut!")