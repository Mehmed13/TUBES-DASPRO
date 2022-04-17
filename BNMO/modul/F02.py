from matriks import *

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

