from matriks import *

def register():
  name = input("Masukkan nama : ") # meminta user untuk memasukkan nama
  username = input("Masukkan username : ") # meminta user untuk memasukkan username
  password = input("Masukkan password : ") # meminta user untuk memasukkan password

  result = readFile("users.csv", username) # memanggil fungsi readFile
  # result = False # memanggil fungsi readFile

  if result == False: # jika result nya adalah False
    register("users.csv", username, name, password) # memanggil function insertData
    print("Username "+ username +" telah berhasil register ke dalam “Binomo”.")
  else: # jika result nya adalah True
    print("Username "+ username +" sudah terpakai, silakan menggunakan username lain.")

if __name__ == "__main__":
    register()
# from splitlines import *
# from matriks import *


# def readFile(file, username):
#     with open(file, "r+") as f:
#         lines = f.read()
#         lines = pecah(lines, "\n")
#         for word in lines:
#             x = pecah(word, ";")
#             if username == x[1]:
# from splitlines import *
# from matriks import *


# def readFile(file, username):
#     with open(file, "r+") as f:
#         lines = f.read()
#         lines = pecah(lines, "\n")
#         for word in lines:
#             x = pecah(word, ";")
#             if username == x[1]:
#                 return True
#     return False  # return False


# def insertData(file, name, username, password):
#     f = open(file, "a")
#     f.write("\n" + name + ";" + username + ";" + password)
#     f.close()


# name = input("Masukkan nama : ")
# username = input("Masukkan username : ")
# password = input("Masukkan password : ")

# result = readFile("users.csv", username)

# if result == False:
#     insertData("users.csv", name, username, password)
#     print("Username " + username + " telah berhasil register ke dalaam “Binomo”.")
# else:
#     print(
#         "Username " + username + " sudah terpakai, silakan menggunakan username lain."
#     )


# # ganti ke csv
# # write gak boleh langsung jadi di save di matriks dulu
# # insert data tetep tapi ga write,dalem insert data pake fungsi append ke matriks
# #

#                 return True
#     return False  # return False


# def insertData(file, name, username, password):
#     f = open(file, "a")
#     f.write("\n" + name + ";" + username + ";" + password)
#     f.close()


# name = input("Masukkan nama : ")
# username = input("Masukkan username : ")
# password = input("Masukkan password : ")

# result = readFile("users.csv", username)

# if result == False:
#     insertData("users.csv", name, username, password)
#     print("Username " + username + " telah berhasil register ke dalaam “Binomo”.")
# else:
#     print(
#         "Username " + username + " sudah terpakai, silakan menggunakan username lain."
#     )


# # ganti ke csv
# # write gak boleh langsung jadi di save di matriks dulu
# # insert data tetep tapi ga write,dalem insert data pake fungsi append ke matriks
# #
