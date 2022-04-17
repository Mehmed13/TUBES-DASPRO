from main import datagameUTAMA
import pecah

#MENAMBAH GAME KE TOKO GAME
def tambah_game():
    global datagametambah
    datagametambah = datagameUTAMA
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
    ID = pecah.hitung_baris_baru(datagametambah)
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
        pecah.append(datagametambah, baris_baru)
        datagametambah[ID][0] = "GAME"+GameID
        datagametambah[ID][1] = nama
        datagametambah[ID][2] = harga
        datagametambah[ID][3] = kategori
        datagametambah[ID][4] = tahun
        datagametambah[ID][5] = stok
        
        print("")
        print("Selamat! Berhasil menambahkan game", nama)
        print("")

    return datagametambah
