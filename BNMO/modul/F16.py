from matriks import *

def save():
    folderName = input("Masukkan nama folder penyimpanan : ")

    result = checkFolder(folderName) # panggil checkFolder yang ada di file matriks
    if result != True: # melakukan pengecekan. Jika folder belum ada, maka ...
        os.mkdir(folderName) # create folder nya
        
        # panggil function create file excel
        register(folderName+"/users.csv", "abc", "abc", "abc") #example
    else:
        resultCheck = checkFile(folderName, "users.csv") # check file udah ada atau belum
        if resultCheck == False:
            register(folderName+"/users.csv", "abc", "abc", "abc") #example
        else:
            os.remove(folderName+"/users.csv") # delete old file
            register(folderName+"/users.csv", "abc", "abc", "abc") # create a new file

if __name__ == "__main__":
    save()