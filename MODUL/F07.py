#Asumsi data pada file tidak mengandung ',' di dalamnya. ',' hanya untuk memisahkan kolom
def split(list, delimiter):
    arr = []
    temp =""
    for char in list:
        if char == delimiter:
            arr += [temp]
            temp =""
        else: 
            temp+= char
    arr+= [temp]
    return arr

def delete(x, data):
    data_del = ""
    for c in data:
        if c != x:
            data_del += c
    return data_del

def hitung_kolom(listgame): #Menghitung jumlah kolom yang ada pada file csv
    banyak_kolom = 0
    for baris in listgame:
        for huruf in baris:
            if huruf == ";": #jika ditemukan tanda ',', berarti terjadi pergantian kolom
                banyak_kolom+=1
        break
    return (banyak_kolom+1) #jumlah kolom = jumlah ',' + 1

def pecah_csv(listgame, datagame): #Mengubah data menjadi bentuk matriks data
    for i in range(hitung_baris(listgame)):
        datagame[i] = split(delete("\n",listgame[i]), ";")
    return datagame
def skemadsc(datagame,atr): #Memproses skema descending (Menurun)
    if atr == "tahun-":
        column = 4
    else: # atr == "harga-"
        column = 2

    if banyak_baris > 1: #Selection sort menurun
        for Pass in range(1, banyak_baris-1):
            IMax = Pass
            for i in range(Pass+1,banyak_baris):
                if float(datagame[i][column]) > float(datagame[IMax][column]):
                    IMax=i
            Temp = datagame[IMax]
            datagame[IMax] = datagame[Pass]
            datagame[Pass] = Temp
    return datagame
def skemaasc(datagame,atr): #Memproses skema ascending (Menurun)
    if atr == "tahun+":
        column = 4
    elif atr == "harga+":
        column = 2
    else: #atr == ""
        column = 0
    if banyak_baris > 1: #selection sort menaik
        for Pass in range(1, banyak_baris-1):
            IMin = Pass
            for i in range(Pass+1,banyak_baris):
                if atr == "": #sorting berdasarkan ID
                    if datagame[i][column] < datagame[IMin][column]:
                        IMin=i
                else:#Sorting berdasarkan harga atau tahun    
                    if float(datagame[i][column]) < float(datagame[IMin][column]):
                        IMin=i
            Temp = datagame[IMin]
            datagame[IMin] = datagame[Pass]
            datagame[Pass] = Temp
    return datagame
def cetaklist(datagame,banyak_kolom, banyak_baris):
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
def hitung_baris(listgame): #Menghitung jumlah baris pada file csv (termasuk header)
    banyak_baris =0
    for baris in listgame:
        banyak_baris +=1
    return banyak_baris
def jumlah_elmt(larik): #Menghitung jumlahan seluruh elemen array numerik 
    jumlah = 0
    for i in larik:
        jumlah+=i
    return jumlah



if __name__ == "__main__":  
    baca = open("game.csv","r") 
    listgame = baca.readlines()        #Penyimpanan isi file pada variabel
    banyak_baris = hitung_baris(listgame)
    banyak_kolom = hitung_kolom(listgame)
    datagame = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)] 
    datagame = pecah_csv(listgame, datagame)
    # Data Kolom
    # ID | NAMA | Harga | Kategori | Tahun Rilis | Stok
    baca.close()
    print(">>> list_game_toko")    
    
    skema_valid = False #inisiasi input tak valid
    while(not skema_valid): #validasi input
    
    #Sistem tidak case-sensitive 
        skema_valid = True
        skema = input('Skema sorting: ').lower()
        if skema == "tahun+" or skema == "harga+" or skema=="":
            datagame = skemaasc(datagame, skema)
            cetaklist(datagame, banyak_kolom, banyak_baris)
        elif skema == "tahun-" or skema == "harga-":
            datagame = skemadsc(datagame, skema)
            cetaklist(datagame, banyak_kolom, banyak_baris)
        else:
            print("Skema sorting tidak valid!")
            skema_valid = False
        print(">>>")



