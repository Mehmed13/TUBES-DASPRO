import os

def hitung_baris(listgame): # function hitung baris
    banyak_baris = 0 # membuat variable penampung
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

def pecah_csv(listgame, datagame): #Mengubah data menjadi bentuk matriks
    for i in range(hitung_baris(listgame)):
        datagame[i] = split(delete("\n",listgame[i]), ";")
    return datagame


#MENGUBAH DATA FILE CSV MENJADI MATRIKS
def load(nama_file): # function load
    global datagame, banyak_baris, banyak_kolom # membuat 3 variable global
    baca = open(nama_file,"r") # membuka dan membaca file csv
    listgame = baca.readlines() # membaca tiap baris pada file csv -> [1,panji,1000,abc,2022,10]
    banyak_baris = hitung_baris(listgame) # memanggil function "hitung_baris"
    banyak_kolom = hitung_kolom(listgame)

    datagame = [["d" for i in range(banyak_kolom)] for j in range(banyak_baris)] 
    datagame = pecah_csv(listgame, datagame)
        # Data Kolom
        # ID | NAMA | Harga | Kategori | Tahun Rilis | Stok
    baca.close()


# UNTUK REGISTRASI - id & saldo
def register(file, username, name, password): # membuat sebuah function register
	insert = open(file, 'a', newline="") # baca file dengan mode append (a)
	insert.writelines(username + ";" + name + ";" + password + ";" + "user" + '\n') # insert username, name, pass, & role
	insert.close() # close connection (close file)

# UNTUK BACA FILE CSV (USERS.CSV)
# ID | USERNAME | NAMA | PASSWORD | ROLE | SALDO
def readFile(file, username): # membuat function read file
	read = open(file, 'r') # baca file dengan mode read (r)
	datas = read.readlines() # membaca tiap baris / line
	for data in datas: # melakukan perulangan untuk membaca tiap baris
		user = split(data, ";") # membaca data per column (separate tanda titik koma)
		if user[0] == username: # mengecek username dari csv sama atau tidak dengan username yang dimasukkan oleh user
			return True # Jika sama, return True

	return False # Jika tidak, return False

# UNTUK CHECK FOLDER
def checkFolder(folderName): # membuat function check folder
	for root in os.walk(folderName): # mengecek list folder yang ada di dalam "folderName"
		if root[0] == folderName: # Jika root index 0 (nama folder) sama dengan "folderName"
			return True # return True
		else: # else
			return False # return False

def checkFile(folderName, fileName): # membuat function check folder
	for root, dirs, files in os.walk(folderName): # mengecek list file yang ada di dalam "folderName"
		for x in files: # looping nama file
			if x == fileName: # jika ada nama file yang sama dengan "fileName"
				return True # return True
		
		return False # return False

# UNTUK BACA FILE CSV (USERS.CSV)
# ID | USERNAME | NAMA | PASSWORD | ROLE | SALDO
def loadUsers(file): # membuat function read file
	read = open(file, 'r') # baca file dengan mode read (r)
	datas = read.readlines() # membaca tiap baris / line
	for data in datas: # melakukan perulangan untuk membaca tiap baris
		users = split(data, ";") # membaca data per column (separate tanda titik koma)
	
	return users