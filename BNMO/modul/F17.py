from F16 import *

answer = ""
while answer != 'y' or answer != 'n' or answer != 'Y' or answer != 'N':
    answer = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah ? (y/n) : ")
    if answer == 'Y' or answer == 'y':
        save()
        exit()
    elif answer == 'N' or answer == 'n' :
        exit()