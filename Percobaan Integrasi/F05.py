from main import datagameUTAMA
import pecah

#MENGUBAH GAME PADA TOKO GAME
def ubah_game():
    global datagameubah
    datagameubah = datagameUTAMA
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
        for i in range (pecah.hitung_baris_baru(datagameubah)):
            if (datagameubah[i][0] == GameIDUbah):
                found = True
                if (NamaGameUbah != ""):
                    datagameubah[i][1] = NamaGameUbah
                if (HargaUbah != ""):
                    datagameubah[i][2] = HargaUbah
                if (KategoriUbah != ""):
                    datagameubah[i][3] = KategoriUbah
                if (TahunUbah != ""):
                    datagameubah[i][4] = TahunUbah

        if (found == False):
            print("")
            print("Tidak ada ID Game yang sesuai!")
            GameIDUbah = ""

    return datagameubah
