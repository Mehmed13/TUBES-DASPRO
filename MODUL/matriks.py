# File untuk menyimpan data csv menjadi sebuah matriks
# matriks = []


# def simpenmatriks(file):
#     with open(file, "r+") as f:
#         f.seek(0)
#         lines = f.read().splitlines()
#         for word in lines:
#             x = word.split(",")
#             matriks.append(x)
#     return matriks
# print(matriks)

# MatriksSemesta = simpenmatriks("users.csv")

#matriks pake fungsi fadil

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

