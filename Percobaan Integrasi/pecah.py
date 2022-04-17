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


#FUNGSI MENAMBAH BARIS BARU PADA MATRIKS
def append(list, e):
    list += [e]

def hitung_baris_baru(matr):
    count = 0
    for e in matr:
        count += 1
    return count


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


baca = open("kepemilikan.csv","r") 
listkepemilikan = baca.readlines()
banyak_baris_kepemilikan = hitung_baris(listkepemilikan)
banyak_kolom_kepemilikan = hitung_kolom(listkepemilikan)

datakepemilikan = [["d" for i in range(banyak_kolom_kepemilikan)] for j in range(banyak_baris_kepemilikan)] 
datakepemilikan = pecah_csv(listkepemilikan, datakepemilikan)
    # Data Kolom
    # ID Game | ID User
baca.close()
