from modul.pecah import *

def riwayat(datariwayat, user_id):

    banyak_baris = length(datariwayat)
    banyak_kolom = hitung_kolom(datariwayat)


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
        datariwayatuser[0] = datariwayat[0] # header
        if datariwayat[i][3] == user_id:
            datariwayatuser[indeks] = datariwayat[i]
            indeks+=1

    cetakdata(datariwayatuser,banyak_kolom-1,banyak_game)