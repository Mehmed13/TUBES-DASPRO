def isValidtitik(x,y,papan): #validasi input
    if (x-1<0 or x-1>2 or y-1<0 or y-1>2): #jika tak valid
        return "Kotak tidak valid."
    elif ( papan[y-1][x-1] == "O" or papan[y-1][x-1]=="X" ): #jika kotak terisi
        return "Kotak sudah terisi. Silakan pilih kotak lain."
    return "valid" #jika valid

#tampilkan papan 
def tampilkan_papan(): 
    print('Status Papan')
    for i in range(3):
        for j in range(3):
            print(papan[i][j], end="")
        print()
    print()

def cek_seri(): #Mengecek apakah game seri
    count = 0
    for i in range(3):
        for j in range(3):
            if papan[i][j] == "X" or papan[i][j] == "O":
                count+= 1
    return (count == 9) #Jika semua elemen telah terisi

def cek_menang (pemain): #mengecek kemenangan pemain
    menang_vertikal = False
    menang_horizontal = False
    menang_diagonal = False

    #cek kemenangan vertikal
    for i in range(3):
        count = 0
        for j in range(3):
            if papan[j][i] == pemain:
                count+=1
        if count == 3:
            menang_vertikal = True
            break
    
    #cek kemenangan horizontal
    for i in range(3):
        count = 0
        for j in range(3):
            if papan[i][j] == pemain:
                count+=1
        if count == 3:
            menang_horizontal = True
            break
    
    #cek kemenangan diagonal
    count = 0
    for i in range(3):
        if papan[i][i] == pemain:
            count+=1
    if count == 3:
        menang_diagonal = True
    count = 0
    for i in range(3):
        if papan[2-i][2-i] == pemain:
            count+=1
    if count == 3:
        menang_diagonal = True

    return menang_vertikal or menang_horizontal or menang_diagonal

def giliran(pemain): #prosedur saat giliran seorang pemain
    global x,y
    print(f'Giliran Pemain "{pemain}"')
    x = int(input("X: "))
    y = int(input("Y: "))
    print()
    #validasi input
    validasi = isValidtitik(x,y,papan)
    while validasi != "valid": #mengulang selama input belum valid
        print(validasi)
        print()
        print(f'Giliran Pemain "{pemain}"')
        x = int(input("X: "))
        y = int(input("Y: "))
        print()
        validasi = isValidtitik(x,y,papan)
        
#Game
print(""">>> tictactoe
Legenda:
# Kosong
X Pemain 1
O Pemain 2
""")

#Setup papan kosong
papan = [['#' for i in range(3)]for i in range(3)]
tampilkan_papan()
while True:
    giliran("X")
    #input sudah valid
    papan[y-1][x-1] = "X" #pengubahan papan

    if cek_menang("X"): #cek kemenangan "X"
        print('Pemain "X" menang.')
        break

    if cek_seri(): #pengecekan apakah game berakhir seri
        print("Seri. Tidak ada yang menang.")
        break
    #ganti giliran
    tampilkan_papan() 
    giliran("O")
    papan[y-1][x-1] = "O" #pengubahan papan
    
    if cek_menang("O"):# cek kemenangan "O"
        print('Pemain "X" menang.')
        break
    tampilkan_papan()

    if cek_seri(): #pengecekan apakah game berakhir seri
        print("Seri. Tidak ada yang menang.")
        break

    



        


