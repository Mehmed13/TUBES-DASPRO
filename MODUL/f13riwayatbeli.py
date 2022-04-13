from F7 import *

user_id = "ayam123"

baca = open("riwayat.csv","r") 
listriwayat = baca.readlines()        #Penyimpanan isi file pada variabel
banyak_baris = hitung_baris(listriwayat)
banyak_kolom = hitung_kolom(listriwayat)
datariwayat = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)] 
datariwayat = pecah_csv(listriwayat, datariwayat)
# Terbentuk Data Kolom
# game_id | nama | harga | user_id | tahun_beli
baca.close()
# sudah terbentuk matriks riwayat.csv

# cari data hanya untuk user_id yang sesuai
banyak_game = 0 #menghitung banyak game yang dimiliki
for i in range(banyak_baris):   
    if datariwayat[i][3] == user_id:
        banyak_game+=1

# inisialisasi matriks data riwayat yang sesuai dengan user
datariwayatuser = [["d" for i in range(banyak_kolom-1)] for j in range(banyak_game+1)]

# ambil data riwayat yang sesuai dengan user id
indeks = 1
for i in range(banyak_baris):
    datariwayatuser[0] = datariwayat[0] # header
    if datariwayat[i][3] == user_id:
        datariwayatuser[indeks] = datariwayat[i]
        indeks+=1

cetaklist(datariwayatuser,banyak_kolom-1,banyak_game+1)