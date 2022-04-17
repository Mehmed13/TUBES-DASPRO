#MISALKAN SAJA SUDAH ADA:
user_id = "ayam123"


#FUNGSI MENGHITUNG DIMENSI FILE CSV
def hitung_baris(listgame):
    banyak_baris = 0
    for baris in listgame:
        banyak_baris = banyak_baris + 1
    return banyak_baris

def hitung_kolom(listgame):
    banyak_kolom = 0
    for baris in listgame:
        for huruf in baris:
            if huruf == ";": #";" adalah tanda ganti kolom
                banyak_kolom = banyak_kolom + 1
        break
    return (banyak_kolom+1) #jumlah kolom = jumlah ";" + 1


#FUNGSI MEMISAH-MISAH DATA FILE CSV
def split(list, delimiter):
    arr = []
    temp = ""
    for char in list:
        if (char == delimiter):
            arr += [temp]
            temp = ""
        else: 
            temp += char
    arr += [temp]
    return arr

def delete(x, data):
    data_del = ""
    for c in data:
        if (c != x):
            data_del += c
    return data_del

def pecah_csv(listgame, datagame): #Mengubah data menjadi bentuk matriks
    for i in range(hitung_baris(listgame)):
        datagame[i] = split(delete("\n",listgame[i]), ";")
    return datagame


#MENGUBAH DATA 2 FILE CSV MENJADI MATRIKS
baca = open("kepemilikan.csv","r") 
listkepemilikan = baca.readlines()
banyak_baris_kepemilikan = hitung_baris(listkepemilikan)
banyak_kolom_kepemilikan = hitung_kolom(listkepemilikan)

datakepemilikan = [["d" for i in range(banyak_kolom_kepemilikan)] for j in range(banyak_baris_kepemilikan)] 
datakepemilikan = pecah_csv(listkepemilikan, datakepemilikan)
    # Data Kolom
    # ID Game | ID User
baca.close()


baca = open("game.csv","r") 
listgame = baca.readlines()
banyak_baris_game = hitung_baris(listgame)
banyak_kolom_game = hitung_kolom(listgame)

datagame = [["d" for i in range(banyak_kolom_game)] for j in range(banyak_baris_game)] 
datagame = pecah_csv(listgame, datagame)
    # Data Kolom
    # ID | NAMA | Harga | Kategori | Tahun Rilis | Stok
baca.close()


#MENAMPUNG GAME ID MILIK USER TERTENTU
banyak_game = 0
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
