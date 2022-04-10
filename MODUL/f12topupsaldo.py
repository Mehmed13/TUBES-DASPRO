def pecah_csv(listgame): #Mengubah data menjadi bentuk matriks data
    bariske = 0 #variabel indeks baris 
    for baris in listgame:
        #inisiasi
        kolom = 0 #variabel indeks kolom
        isikolom = "" 
        for i in range(length(baris)): #Proses split 
            if baris[i] == ';':
                daftaruser[bariske][kolom] = isikolom
                isikolom = ""
                kolom+=1
            elif baris[i] ==' ' and baris[i-1] == ';': #spasi setelah tanda titik koma diabaikan
                continue
            elif baris[i]== '\n':
                break
            else:
                isikolom+=baris[i] #konkantenasi isi kolom
        daftaruser[bariske][kolom] = isikolom #Pengisian elemen matriks
        bariske +=1
    return daftaruser

def hitung_kolom(listgame): #Menghitung jumlah kolom yang ada pada file csv
    banyak_kolom = 0
    for baris in listgame:
        for huruf in baris:
            if huruf == ";": #jika ditemukan tanda ';', berarti terjadi pergantian kolom
                banyak_kolom+=1
        break
    return (banyak_kolom+1) #jumlah kolom = jumlah ';' + 1

def hitung_baris(listgame): #Menghitung jumlah baris pada file csv (termasuk header)
    banyak_baris = 0
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

baca = open("user.csv", "r")
user = baca.readlines()
banyak_kolom = hitung_kolom(user)
banyak_baris = hitung_baris(user)
daftaruser = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)] 
daftaruser = pecah_csv(user)


username = input("Masukan username: ")
saldo = int(input("Masukan saldo: "))
