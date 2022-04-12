from F7 import *

#Ceritanya di program asli, udah ada user id
user_id = 'ayam123'

def carigame_inventory():
    #Collect data game id yg dimiliki user
    baca = open("Kepemilikan.csv","r") 
    listKepemilikan = baca.readlines()        #Penyimpanan isi file pada variabel
    banyak_baris = hitung_baris(listKepemilikan)
    banyak_kolom = hitung_kolom(listKepemilikan)
    datakepemilikan = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)] 
    datakepemilikan = pecah_csv(listKepemilikan, datakepemilikan)
    # Data Kolom
    # game_id | user_id
    baca.close()
    #Sudah terbentuk matriks kepemilikan.csv

    #Buat list penampung game id yang dimiliki user

    banyak_game = 0 #menghitung banyak game yang dimiliki
    for i in range(banyak_baris):   
        if datakepemilikan[i][1] == user_id:
            banyak_game+=1

    list_gameid = ["d" for i in range(banyak_game)] #inisiasi list game id yang dimiliki user
    count = 0 #menandakan indeks game ke-count
    for i in range(banyak_baris):
        if datakepemilikan[i][1] == user_id:
            list_gameid[count] = datakepemilikan[i][0] #pengisian list game id yang dimiliki user
            count += 1        

    #Pengambilan data game dari game.csv
    baca = open("game.csv","r") 
    listgame = baca.readlines()        #Penyimpanan isi file pada variabel
    banyak_baris_gamecsv = hitung_baris(listgame)
    banyak_kolom_gamecsv = hitung_kolom(listgame)
    datagame = [["d" for i in range(banyak_kolom_gamecsv)] for j in range(banyak_baris_gamecsv)] 
    datagame = pecah_csv(listgame, datagame)
    # Data Kolom
    # ID | NAMA | Harga | Kategori | Tahun Rilis | Stok
    baca.close()

    #pengambilan data game yang dimiliki user
    datagameuser = [['d' for i in range(banyak_kolom_gamecsv)] for j in range(banyak_game+1)] #inisiasi matriks data game yang dimiliki user

    #Pengisian data game yang dimiliki user
    indeks = 1 #penanda indeks
    for i in range(banyak_baris):
        datagameuser[0] = datagame[0]   #header
        for j in range(banyak_game):#indexing untuk list_gameid
            if datagame[i][0] == list_gameid[j]:
                datagameuser[indeks] = datagame[i] #pengisian
                indeks += 1

    #input parameter searching
    print(">>> search_my_game")
    id_game = input("Masukkan ID Game: ")
    tahunrilis = input("Masukkan Tahun Rilis Game: ")

    #searching
    if id_game == "" and tahunrilis == "":#tanpa parameter
        print('Daftar game pada inventory yang memenuhi kriteria: ')
        if banyak_game == 0:
            print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
        else:    
            cetaklist(datagameuser,banyak_kolom_gamecsv,banyak_game+1)
    elif id_game != "" and tahunrilis == "": #searching berdasarkan game id
        print('Daftar game pada inventory yang memenuhi kriteria: ')
        gameid_sesuai = 0
        for i in range(1,banyak_game+1): #mencari banyaknya game id yang memenuhi
            if datagameuser[i][0] == id_game:
                gameid_sesuai+=1
        datasearch_gameid = [['d' for i in range(banyak_kolom_gamecsv)] for j in range(gameid_sesuai+1)]#inisiasi datasearch, +1 karena header
        datasearch_gameid[0]=datagameuser[0] #baris header
        indeks = 1 #penanda indeks
        for i in range(1,banyak_game+1):
            if datagameuser[i][0] == id_game:
                datasearch_gameid[indeks] =  datagameuser[i] #pengisian datasearch
                indeks += 1
        if gameid_sesuai == 0:
            print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
        else:
            cetaklist(datasearch_gameid,banyak_kolom_gamecsv,gameid_sesuai+1) 
    elif id_game == "" and tahunrilis != "":
        tahunrilis_sesuai = 0
        for i in range(1,banyak_game+1): #mencari banyaknya game id yang memenuhi
            if datagameuser[i][4] == tahunrilis:
                tahunrilis_sesuai+=1
        datasearch_tahunrilis = [['d' for i in range(banyak_kolom)] for j in range(tahunrilis_sesuai+1)]#inisiasi datasearch, +1 karena header
        datasearch_tahunrilis[0]=datagameuser[0] #header
        indeks = 1 #penanda indeks   
        for i in range(1,banyak_game+1):
            if datagameuser[i][4] == tahunrilis:
                datasearch_tahunrilis[indeks] =  datagameuser[i] #pengisian datasearch
                indeks += 1
        if tahunrilis_sesuai == 0:
            print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
        else:
            cetaklist(datasearch_tahunrilis, banyak_kolom_gamecsv, tahunrilis_sesuai+1) 

    else: #id_game != "" and tahunrilis != ""
        semua_sesuai = 0
        for i in range(1,banyak_game+1): #mencari banyaknya game id yang memenuhi
            if datagameuser[i][0] == id_game and datagameuser[i][4] == tahunrilis:
                semua_sesuai+=1
        datasearch_duaparameter = [['d' for i in range(banyak_kolom)] for j in range(semua_sesuai+1)]#inisiasi datasearch, +1 karena header
        datasearch_duaparameter[0]=datagameuser[0] #header
        indeks = 1 #penanda indeks   
        for i in range(1,banyak_game+1):
            if datagameuser[i][4] == id_game:
                datasearch_duaparameter[indeks] =  datagameuser[i] #pengisian datasearch
                indeks+=1
        if semua_sesuai == 0:
            print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
        else:
            cetaklist(datasearch_duaparameter, banyak_kolom_gamecsv, semua_sesuai+1) 
    print(">>>")
if __name__ == "__main__":
    carigame_inventory()
