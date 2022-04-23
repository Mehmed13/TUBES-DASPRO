from modul.F16 import *

def func_exit(datagameUTAMA, datakepemilikanUTAMA, datariwayatUTAMA, datauserUTAMA):
    answer = ""
    while answer != 'y' or answer != 'n' or answer != 'Y' or answer != 'N':
        answer = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah ? (y/n) : ")
        if answer == 'Y' or answer == 'y':
            save(datagameUTAMA,datakepemilikanUTAMA,datariwayatUTAMA,datauserUTAMA)
            exit()
        elif answer == 'N' or answer == 'n' :
            exit()
