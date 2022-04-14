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


#MENGUBAH STOK PADA TOKO GAME
def ubah_stok():
    global datagame
    found = False

    GameIDUbah = str(input("Masukkan ID game: "))
    #Memastikan ID Game Terisi
    while (GameIDUbah == ""):
        print("")
        print("ID Game harus dimasukkan agar dapat mengubah data!") 
        GameIDUbah = str(input("Masukkan ID game: "))
    #Validasi ID Game
    for i in range (banyak_baris):
        if (datagame[i][0] == GameIDUbah):
            found = True
    if (found == False):
        print("")
        print("Tidak ada game dengan ID tersebut!")

    #Menerima Jumlah Penambahan atau Pengurangan Stok
    if (found == True):
        StokUbah = str(input("Masukkan jumlah: "))
        for i in range (banyak_baris):
            if (datagame[i][0] == GameIDUbah):
                if (StokUbah == "") or (StokUbah == "0"):
                    print("Stok game", datagame[i][1], "tidak berubah. Stok sekarang:", datagame[i][5])
                elif (int(StokUbah) < 0):
                    if (int(datagame[i][5])+int(StokUbah) < 0):
                        print("Stok game", datagame[i][1], "gagal dikurangi karena stok kurang. Stok sekarang:", datagame[i][5], "(<", str(abs(int(StokUbah)))+")")
                    else:
                        print("Stok game", datagame[i][1], "berhasil dikurangi. Stok sekarang:", int(datagame[i][5])+int(StokUbah))
                        datagame[i][5] = str(int(datagame[i][5]) + int(StokUbah))
                else:
                    print("Stok game", datagame[i][1], "berhasil ditambahkan. Stok sekarang:", int(datagame[i][5])+int(StokUbah))
                    datagame[i][5] = str(int(datagame[i][5]) + int(StokUbah))
