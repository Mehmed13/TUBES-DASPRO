from pecah import datagame
datagameUTAMA = datagame

from pecah import datakepemilikan
datakepemilikanUTAMA = datakepemilikan

#ALGORIMA MAIN
if __name__ == "__main__":
    print("Menu:")
    print("4. tambah_game")
    print("5. ubah_game")
    print("6. ubah_stok")
    print("9. list_game")
    print("")

    process = True
    cmd = str(input(">>> "))

    while (process == True):
        if (cmd == "tambah_game"):
            import F04
            datagameUTAMA = F04.tambah_game()
            cmd = str(input(">>> "))
        elif (cmd == "ubah_game"):
            import F05
            datagameUTAMA = F05.ubah_game()
            print("")
            cmd = str(input(">>> "))
        elif (cmd == "ubah_stok"):
            import F06
            datagameUTAMA = F06.ubah_stok()
            print("")
            cmd = str(input(">>> "))
        elif (cmd == "list_game"):
            import F09
            F09.list_game()
            print("")
            cmd = str(input(">>> "))
        else:
            process = False
    
    print(datagameUTAMA)
