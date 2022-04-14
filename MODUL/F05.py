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


#MENGUBAH DATA FILE CSV MENJADI MATRIKS
baca = open("game.csv","r") 
listgame = baca.readlines()
banyak_baris = hitung_baris(listgame)
banyak_kolom = hitung_kolom(listgame)

datagame = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)] 
datagame = pecah_csv(listgame, datagame)
    # Data Kolom
    # ID | NAMA | Harga | Kategori | Tahun Rilis | Stok
baca.close()


#MENGUBAH GAME PADA TOKO GAME
def ubah_game():
    global datagame
    GameIDUbah = ""
    found = False

    while (found == False):
        NamaGameUbah = ""
        KategoriUbah = ""
        TahunUbah = ""
        HargaUbah = ""
        
        GameIDUbah = str(input("Masukkan ID game: "))
        NamaGameUbah = str(input("Masukkan nama game: "))
        KategoriUbah = str(input("Masukkan kategori: "))
        TahunUbah = str(input("Masukkan tahun rilis: "))
        HargaUbah = str(input("Masukkan harga: "))

        while (GameIDUbah == ""):
            print("")
            print("ID Game harus dimasukkan agar dapat mengubah data!")
            NamaGameUbah = ""
            KategoriUbah = ""
            TahunUbah = ""
            HargaUbah = ""
            
            GameIDUbah = str(input("Masukkan ID game: "))
            NamaGameUbah = str(input("Masukkan nama game: "))
            KategoriUbah = str(input("Masukkan kategori: "))
            TahunUbah = str(input("Masukkan tahun rilis: "))
            HargaUbah = str(input("Masukkan harga: "))

        #Validasi ID Game
        for i in range (banyak_baris):
            if (datagame[i][0] == GameIDUbah):
                found = True
                if (NamaGameUbah != ""):
                    datagame[i][1] = NamaGameUbah
                if (HargaUbah != ""):
                    datagame[i][2] = HargaUbah
                if (KategoriUbah != ""):
                    datagame[i][3] = KategoriUbah
                if (TahunUbah != ""):
                    datagame[i][4] = TahunUbah

        if (found == False):
            print("")
            print("Tidak ada ID Game yang sesuai!")
            GameIDUbah = ""
