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


#MENAMBAH GAME KE TOKO GAME
def tambah_game():
    global datagame
    nama = ""
    kategori = ""
    tahun = ""
    harga = ""
    stok = ""

    nama = str(input("Masukkan nama game: "))
    kategori = str(input("Masukkan kategori: "))
    tahun = str(input("Masukkan tahun rilis: "))
    harga = str(input("Masukkan harga: "))
    stok = str(input("Masukkan stok awal: "))

    while (nama == "") or (kategori == "") or (tahun == "") or (harga == "") or (stok == ""):
        print("")
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        nama = ""
        kategori = ""
        tahun = ""
        harga = ""
        stok = ""

        nama = str(input("Masukkan nama game: "))
        kategori = str(input("Masukkan kategori: "))
        tahun = str(input("Masukkan tahun rilis: "))
        harga = str(input("Masukkan harga: "))
        stok = str(input("Masukkan stok awal: "))

    #Terminasi
    ID = hitung_baris_baru(datagame)
    if (ID > 999):
        print("Sudah tidak bisa menambah game")
    else:
        if (ID < 10):
            GameID = "00" + str(ID)
        elif (ID >= 10) and (ID <= 99):
            GameID = "0" + str(ID)
        else:
            GameID = str(ID)

        baris_baru = ["" for i in range(6)]
        append(datagame, baris_baru)
        datagame[ID][0] = "GAME"+GameID
        datagame[ID][1] = nama
        datagame[ID][2] = harga
        datagame[ID][3] = kategori
        datagame[ID][4] = tahun
        datagame[ID][5] = stok
        
        print("")
        print("Selamat! Berhasil menambahkan game", nama)
        print("")
