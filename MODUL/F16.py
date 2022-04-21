import os
from unicodedata import name
from modul.pecah import * 

def save(MATRIKS_GAME, MATRIKS_KEPEMILIKAN, MATRIKS_RIWAYAT, MATRIKS_USER):
    while(True):
        userinput = input("Masukkan nama folder penyimpanan: ")

        if (len(userinput) == 0):
            print("Nama file tidak boleh kosong.") 
        else:
            temp_dir = os.path.join(os.getcwd(), userinput)
            if not (os.path.exists(temp_dir)):
                os.makedirs(temp_dir)

            counter = 0
            with open(os.path.join(temp_dir, "game.csv"), 'w') as f:
                for baris in MATRIKS_GAME:
                    temp = ""
                    banyak_kolom = 0
                    for kolom in baris :
                        banyak_kolom = banyak_kolom + 1
                    counter=0
                    for kolom in baris :
                        if(counter == banyak_kolom -1) :
                            temp = temp + str(kolom)
                        else:
                            temp = temp + str(kolom) + ";"
                        counter = counter + 1
                    f.write(temp + '\n')
            with open(os.path.join(temp_dir, "kepemilikan.csv"), 'w') as f:
                for baris in MATRIKS_KEPEMILIKAN:
                    temp = ""
                    banyak_kolom = 0
                    for kolom in baris :
                        banyak_kolom = banyak_kolom + 1
                    counter=0
                    for kolom in baris :
                        if(counter == banyak_kolom -1) :
                            temp = temp + str(kolom)
                        else:
                            temp = temp + str(kolom) + ";"
                        counter = counter + 1
                    f.write(temp + '\n')
            with open(os.path.join(temp_dir, "riwayat.csv"), 'w') as f:
                for baris in MATRIKS_RIWAYAT:
                    temp = ""
                    banyak_kolom = 0
                    for kolom in baris :
                        banyak_kolom = banyak_kolom + 1
                    counter=0
                    for kolom in baris :
                        if(counter == banyak_kolom -1) :
                            temp = temp + str(kolom)
                        else:
                            temp = temp + str(kolom) + ";"
                        counter = counter + 1
                    f.write(temp + '\n')
            with open(os.path.join(temp_dir, "user.csv"), 'w') as f:
                for baris in MATRIKS_USER:
                    temp = ""
                    banyak_kolom = 0
                    for kolom in baris :
                        banyak_kolom = banyak_kolom + 1
                    counter=0
                    for kolom in baris :
                        if(counter == banyak_kolom -1) :
                            temp = temp + str(kolom)
                        else:
                            temp = temp + str(kolom) + ";"
                        counter = counter + 1
                    f.write(temp + '\n')
            print("Save sukses!")
            break
