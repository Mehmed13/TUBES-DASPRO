def pecah_csv(listgame): #Mengubah data menjadi bentuk matriks data
    bariske = 0 #variabel indeks baris 
    for baris in listgame:
        #inisiasi
        kolom = 0 #variabel indeks kolom
        isikolom = "" 
        for i in range(length(baris)): #Proses split 
            if baris[i] == ';':
                daftariwayat[bariske][kolom] = isikolom
                isikolom = ""
                kolom+=1
            elif baris[i] ==' ' and baris[i-1] == ';': #spasi setelah tanda titik koma diabaikan
                continue
            elif baris[i]== '\n':
                break
            else:
                isikolom+=baris[i] #konkantenasi isi kolom
        daftariwayat[bariske][kolom] = isikolom #Pengisian elemen matriks
        bariske +=1
    return daftariwayat

def hitung_kolom(listgame): #Menghitung jumlah kolom yang ada pada file csv
    banyak_kolom = 0
    for baris in listgame:
        for huruf in baris:
            if huruf == ";": #jika ditemukan tanda ';', berarti terjadi pergantian kolom
                banyak_kolom+=1
        break
    return (banyak_kolom+1) #jumlah kolom = jumlah ';' + 1

def hitung_baris(listgame): #Menghitung jumlah baris pada file csv (termasuk header)
    banyak_baris =0
    for baris in listgame:
        banyak_baris +=1
    return banyak_baris

def length(isi): #Menghitung panjang array
    count = 0
    for e in isi:
        count+=1
    return count

def maks(larik): #Menghitung nilai maksimum suatu array
    maks = larik[0]
    for i in range(1, length(larik)):
        if larik[i] > maks:
            maks = larik[i]
    return maks

def jumlah_elmt(larik): #Menghitung jumlahan seluruh elemen array numerik 
    jumlah = 0
    for i in larik:
        jumlah+=i
    return jumlah

def cetaklist(datagame):
    #Membentuk list panjang maks masing-masing kolom untuk format
    panjang_makskolom = [0 for i in range(banyak_kolom)]
    for i in range(banyak_kolom):
        panjang_isikolom = [0 for i in range(banyak_baris)]
        for j in range(banyak_baris):
            panjang_isikolom[j] = length(datagame[j][i])
        panjang_makskolom[i] = maks(panjang_isikolom)+2 #1 whitespace sebelum dan sesudah isi kolom panjang maks
    
    #cetak list
    nomor = 0 #inisiasi
    for i in range(banyak_baris):
        if i == 0:
            print("  ",end="")
        else:
            print(f'{nomor}.', end="") #untuk nomor
        for j in range(banyak_kolom):
            if j == banyak_kolom-1: #kolom terakhir
                print(" "+datagame[i][j])
            else:
                print(" "+datagame[i][j], end="")
                for k in range(panjang_makskolom[j]-1-length(datagame[i][j])): #whitepace setelah isi kolom
                    print(" ", end='')
                print('|',end='')
        if i == 0:
            for j in range(jumlah_elmt(panjang_makskolom)+banyak_kolom+1): #Batas antara header dan isi tabel
                print("_",end="")
            print()
            
        nomor += 1

baca = open("riwayat.csv", "r")
riwayat = baca.readlines()
banyak_kolom = hitung_kolom(riwayat)
banyak_baris = hitung_baris(riwayat)

if banyak_baris == 1:
    print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    print(">>>")
else:
    daftariwayat = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)] 
    daftariwayat = pecah_csv(riwayat)
    cetaklist(daftariwayat)

baca.close()