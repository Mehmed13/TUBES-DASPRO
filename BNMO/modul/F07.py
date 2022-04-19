from modul.pecah import*

#Asumsi data pada file tidak mengandung ';' di dalamnya. ';' hanya untuk memisahkan kolom
def skemadsc(datagame,banyak_baris,atr): #Memproses skema descending (Menurun)
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
def skemaasc(datagame,banyak_baris,atr): #Memproses skema ascending (Menurun)
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
                if atr != "":#Sorting berdasarkan harga atau tahun    
                    if float(datagame[i][column]) < float(datagame[IMin][column]):
                        IMin=i
            Temp = datagame[IMin]
            datagame[IMin] = datagame[Pass]
            datagame[Pass] = Temp
    return datagame

def list_game_toko(datagame):    
    banyak_baris = length(datagame)
    banyak_kolom = length(datagame[0])
    skema_valid = False #inisiasi input tak valid
    while(not skema_valid): #validasi input
    
    #Sistem tidak case-sensitive 
        skema_valid = True
        skema = input('Skema sorting: ').lower()
        if skema == "tahun+" or skema == "harga+" or skema=="":
            datagame = skemaasc(datagame, banyak_baris, skema)
            cetakdata(datagame, banyak_kolom, banyak_baris)
        elif skema == "tahun-" or skema == "harga-":
            datagame = skemadsc(datagame, banyak_baris, skema)
            cetakdata(datagame, banyak_kolom, banyak_baris)
        else:
            print("Skema sorting tidak valid!")
            skema_valid = False
        print(">>>")
