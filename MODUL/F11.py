# F11 - Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis
from F7 import *

def search(datagame, parameter, isi):
    if isi =="": #jika parameter kosong
        datasearch = [['d' for i in range(banyak_kolom)]for j in range(banyak_baris-1)]
        for i in range(1,banyak_baris):
            datasearch[i-1] = datagame[i] #menyalin datagame ke datasearch tanpa header
    
    else:
        #penentuan kolom yang akan digunakan berdasarkan jenis parameter 
        if parameter == "id":
            kolom = 0
        elif parameter == "nama":
            kolom = 1
        elif parameter == "harga":
            kolom = 2
        elif parameter == "kategori":
            kolom = 3
        else: #parameter == "tahunrilis"
            kolom = 4
        banyak_sesuai = 0
        for i in range(banyak_baris): #mencari banyaknya baris untuk pendefinisian matriks
            if datagame[i][kolom] == isi:
                banyak_sesuai += 1
        
        datasearch = [['d' for i in range(banyak_kolom)]for j in range(banyak_sesuai)] #pendefinisian matriks

        indeks = 0
        for i in range(1,banyak_baris):
            if datagame[i][kolom] == isi:
                datasearch[indeks] = datagame[i] #pengisian datasearch
                indeks += 1
    return datasearch

def carigame_toko():
    global banyak_baris, banyak_kolom
    baca = open("game.csv","r") 
    listgame = baca.readlines()        #Penyimpanan isi file pada variabel
    banyak_baris = hitung_baris(listgame)
    banyak_kolom = hitung_kolom(listgame)
    datagame = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)] 
    datagame = pecah_csv(listgame, datagame)
    # Data Kolom
    # ID | NAMA | Harga | Kategori | Tahun Rilis | Stok
    baca.close()


    print(">>> search_game_at_store")
    #Input parameter
    id_game = input("Masukkan ID Game: ")
    nama_game = input("Masukkan Nama Game: ")
    harga_game = input("Masukkan Harga Game: ")
    kategori_game = input("Masukkan Kategori Game: ")
    tahunrilis_game = input("Masukkkan Tahun Rilis Game: ")

    #Searching

    #Mengambil data hasil search setiap parameter
    datasearch_id = search(datagame,"id",id_game)
    datasearch_nama = search(datagame,"nama",nama_game)
    datasearch_harga = search(datagame,"harga", harga_game)
    datasearch_kategori = search(datagame, "kategori", kategori_game)
    datasearch_tahunrilis = search(datagame, "tahunrilis", tahunrilis_game)

    #Membuat matriks datasearch_final
    list_banyakbaris = [0 for i in range(5)] #inisiasi list untuk menampung banyak baris search masing-masing parameter
    list_banyakbaris[0] = hitung_baris(datasearch_id)
    list_banyakbaris[1] = hitung_baris(datasearch_nama)
    list_banyakbaris[2] = hitung_baris(datasearch_harga)
    list_banyakbaris[3] = hitung_baris(datasearch_kategori)
    list_banyakbaris[4] = hitung_baris(datasearch_tahunrilis) 

    banyakbaris_final = 0
    for i in range(list_banyakbaris[0]): #penghitungan banyak baris untuk datasearchfinal
        for j in range(list_banyakbaris[1]):
            for k in range(list_banyakbaris[2]):
                for l in range(list_banyakbaris[3]):
                    for m in range(list_banyakbaris[4]):
                        if datasearch_id[i] == datasearch_nama[j] ==datasearch_harga[k] == datasearch_kategori[l] == datasearch_tahunrilis[m]:
                            banyakbaris_final +=1
        
    datasearch_final = [['d' for i in range(banyak_kolom)]for j in range(banyakbaris_final+1)] #+1 untuk header

    datasearch_final[0] = datagame[0] #header

    indeks = 1
    for i in range(list_banyakbaris[0]): #penghitungan banyak baris untuk datasearchfinal
        for j in range(list_banyakbaris[1]):
            for k in range(list_banyakbaris[2]):
                for l in range(list_banyakbaris[3]):
                    for m in range(list_banyakbaris[4]):
                        if datasearch_id[i] == datasearch_nama[j] ==datasearch_harga[k] == datasearch_kategori[l] == datasearch_tahunrilis[m]:
                            datasearch_final[indeks] = datasearch_id[i] #bisa pilih salah satu datasearch
                            indeks +=1 


    print("Daftar game pada inventory yang memenuhi kriteria: ")
    if banyakbaris_final == 0:
        print("Tidak ada game pada toko yang memenuhi kriteria")
    else:
        cetaklist(datasearch_final,banyak_kolom,banyakbaris_final+1)                     
    print(">>>")

if __name__ == "__main__":
    carigame_toko()
