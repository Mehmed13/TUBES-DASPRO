def hitung_baris(listgame):
    banyak_baris = 0
    for baris in listgame:
        banyak_baris = banyak_baris + 1
    return banyak_baris

baca = open("game.csv","r") 
listgame = baca.readlines()
banyak_baris = hitung_baris(listgame)
baca.close()

def tambah_game():
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
    ID = banyak_baris
    if (ID > 999):
        print("Sudah tidak bisa menambah game")
    else:
        if (ID < 10):
            GameID = "00" + str(ID)
        elif (ID >= 10) and (ID <= 99):
            GameID = "0" + str(ID)
        else:
            GameID = str(ID)
        print("")
        print("Selamat! Berhasil menambahkan game", nama)
        print("")

        tulis = open("game.csv", "a", newline="")
        tulis.writelines(f'GAME{GameID};{nama};{harga};{kategori};{tahun};{stok}\n')
        tulis.close()
