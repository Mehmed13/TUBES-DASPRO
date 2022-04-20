from modul.pecah import *

def riwayat(datariwayat, user_id):

    banyak_baris = length(datariwayat)
    banyak_kolom = length(datariwayat[0])


    # cari data hanya untuk user_id yang sesuai
    banyak_game = 0 #menghitung banyak game yang dimiliki
    for i in range(banyak_baris):   
        if datariwayat[i][3] == user_id:
            banyak_game+=1

    # pengambilan data riwayat yang sesuai dengan user
    datariwayatuser = [["d" for i in range(banyak_kolom-1)] for j in range(banyak_game+1)]

    # ambil data riwayat yang sesuai dengan user id
    indeks = 1
    for i in range(banyak_baris):
        indeks_kolom = 0
        for k in range(banyak_kolom):
            if k != 3:
                datariwayatuser[0][indeks_kolom] = datariwayat[0][k] # header
                indeks_kolom+=1
        indeks_kolom = 0
        if datariwayat[i][3] == user_id: #mengisi matriks datariwayat user
            for j in range(banyak_kolom):
                if j != 3:
                    datariwayatuser[indeks][indeks_kolom] = datariwayat[i][j]
                    indeks_kolom+=1
            indeks+=1

    cetakdata(datariwayatuser,banyak_kolom-1,banyak_game+1)
