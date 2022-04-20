import os
#FUNGSI CEK KEBERADAAN FOLDER
def checkFolder(folderName): # membuat function check folder
	for root in os.walk(folderName): # mengecek list folder yang ada di dalam "folderName"
		if root[0] == folderName: # Jika root index 0 (nama folder) sama dengan "folderName"
			return True # return True
		else: # else
			return False # return False

#FUNGSI MENCARI NILAI MAKS PADA ARRAY
def maks(larik): #Menghitung nilai maksimum suatu array
    maks = larik[0]
    for i in range(1, length(larik)):
        if larik[i] > maks:
            maks = larik[i]
    return maks

#FUNGSI MENGHITUNG DIMENSI FILE CSV
def length(listgame):
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

#FUNGSI MENAMBAH BARIS BARU PADA MATRIKS
def append(list, e):
    list += [e]
    return list
# FUNGSI MENGUBAH DATA FILE CSV MENJADI MATRIKS
def csv_to_matrix(foldername,filename):
    baca = open(f"{foldername}\\{filename}","r") 
    listdata = baca.readlines()
    banyak_baris = length(listdata)
    banyak_kolom = hitung_kolom(listdata)
    datagame = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)]
    for i in range(length(listdata)):
        datagame[i] = split(delete("\n",listdata[i]), ";") 
    baca.close()
    return datagame

# FUNGSI MENCETAK DATA
def cetakdata(datagame,banyak_kolom, banyak_baris):
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
            for j in range(banyak_kolom): #Batas antara header dan isi tabel
                for k in range(panjang_makskolom[j]):
                    print("_",end="")
            for j in range(banyak_kolom-1):
                print("_", end="")
            print("___")
            
        nomor += 1




# Data Kolom kepemilikan.csv
# ID Game | ID User

# Data Kolom game.csv
# ID | NAMA | Harga | Kategori | Tahun Rilis | Stok

# Data Kolom user.csv
# ID | Username | Nama | Password | Role | Saldo

# Data Kolom riwayat.csv
# GAME ID | Nama | Harga | User ID | Tahun Beli
