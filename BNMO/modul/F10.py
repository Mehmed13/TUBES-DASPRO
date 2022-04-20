from modul.pecah import *

def search_my_game(datakepemilikan, datagame, user_id):
    #proses datakepemilikan
    banyak_baris = length(datakepemilikan)

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

    #proses datagame
    banyak_baris_gamecsv = length(datagame)
    banyak_kolom_gamecsv = length(datagame[0])

    #pengambilan data game yang dimiliki user
    datagameuser = [['d' for i in range(banyak_kolom_gamecsv)] for j in range(banyak_game+1)] #inisiasi matriks data game yang dimiliki user

    #Pengisian data game yang dimiliki user
    indeks = 1 #penanda indeks
    for i in range(banyak_baris_gamecsv):
        datagameuser[0] = datagame[0]   #header
        for j in range(banyak_game):#indexing untuk list_gameid
            if datagame[i][0] == list_gameid[j]:
                datagameuser[indeks] = datagame[i] #pengisian
                indeks += 1

    #input parameter searching
    id_game = input("Masukkan ID Game: ")
    tahunrilis = input("Masukkan Tahun Rilis Game: ")

    #searching
    print('Daftar game pada inventory yang memenuhi kriteria: ')
    if id_game == "" and tahunrilis == "":#tanpa parameter
        if banyak_game == 0:
            print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
        else:    
            cetakdata(datagameuser,banyak_kolom_gamecsv,banyak_game+1)
    elif id_game != "" and tahunrilis == "": #searching berdasarkan game id
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
            cetakdata(datasearch_gameid,banyak_kolom_gamecsv,gameid_sesuai+1) 
    elif id_game == "" and tahunrilis != "":
        tahunrilis_sesuai = 0
        for i in range(1,banyak_game+1): #mencari banyaknya game id yang memenuhi
            if datagameuser[i][4] == tahunrilis:
                tahunrilis_sesuai+=1
        datasearch_tahunrilis = [['d' for i in range(banyak_kolom_gamecsv)] for j in range(tahunrilis_sesuai+1)]#inisiasi datasearch, +1 karena header
        datasearch_tahunrilis[0]=datagameuser[0] #header
        indeks = 1 #penanda indeks   
        for i in range(1,banyak_game+1):
            if datagameuser[i][4] == tahunrilis:
                datasearch_tahunrilis[indeks] =  datagameuser[i] #pengisian datasearch
                indeks += 1
        if tahunrilis_sesuai == 0:
            print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
        else:
            cetakdata(datasearch_tahunrilis, banyak_kolom_gamecsv, tahunrilis_sesuai+1) 

    else: #id_game != "" and tahunrilis != ""
        semua_sesuai = 0
        for i in range(1,banyak_game+1): #mencari banyaknya game id yang memenuhi
            if datagameuser[i][0] == id_game and datagameuser[i][4] == tahunrilis:
                semua_sesuai+=1
        datasearch_duaparameter = [['d' for i in range(banyak_kolom_gamecsv)] for j in range(semua_sesuai+1)]#inisiasi datasearch, +1 karena header
        datasearch_duaparameter[0]=datagameuser[0] #header
        indeks = 1 #penanda indeks   
        for i in range(1,banyak_game+1):
            if datagameuser[i][0] == id_game:
                datasearch_duaparameter[indeks] =  datagameuser[i] #pengisian datasearch
                indeks+=1
        if semua_sesuai == 0:
            print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
        else:
            cetakdata(datasearch_duaparameter, banyak_kolom_gamecsv, semua_sesuai+1) 
    print(">>>")
