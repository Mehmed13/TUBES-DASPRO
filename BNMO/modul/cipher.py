from modul.pecah import*

#Password sudah dipastikan hanya terdiri dari alfabet A-Z, a-z, "-", "_", atau angka 0..9

def E(a,b,m,x): #enkripsi 
    y = (a*x + b)%m
    return y

def D(ai,b,m,y):
    x = (ai*(y-b))%m
    return x

def encrypt(x):
    if x =="-": 
        char = "_"
    elif x == "_":
        char = "-"
    else:
        a = 7
        b = 11
        if ord(x)>= 48 and ord(x)<= 57: #enkripsi untuk character angka
            m = 10
            xi = ord(x) - 48 #agar nilai xi antara 0..9
            yi = E(a,b,m,xi)
            y = yi + 48 #membalikkan ke dalam ascii code
        
        else: #alfabet
            m = 26
            if ord(x)>= 65 and ord(x)<= 90: #enkripsi untuk huruf kapital
                xi = ord(x) - 65 #agar nilai xi antara 0..25
                yi = E(a,b,m,xi)
                y = yi + 65 #mengembalikan ke dalam ascii code
                
            elif ord(x) >= 97 and ord(x) <= 122: #untuk huruf bukan kapital
                xi = ord(x) - 97 #agar nilai xi antara 0..25
                yi = E(a,b,m,xi)
                y = yi + 97
        char = chr(y) #memunculkan karakter
    return char

def decrypt(y):
    if y =="-": 
        char = "_"
    elif y == "_":
        char = "-"
    else:
        b = 11
        if ord(y)>= 48 and ord(y)<= 57: #dekripsi untuk character angka
            ai = 3
            m = 10
            yi = ord(y) - 48 #agar nilai yi antara 0..9
            xi = D(ai,b,m,yi)
            x = xi + 48 #membalikkan ke dalam ascii code
        
        else: #alfabet
            ai = 15
            m = 26
            if ord(y)>= 65 and ord(y)<= 90: #dekripsi untuk huruf kapital
                yi = ord(y) - 65 #agar nilai yi antara 0..25
                xi = D(ai,b,m,yi)
                x = xi + 65 #mengembalikan ke dalam ascii code
                
            elif ord(y) >= 97 and ord(y) <= 122: #untuk huruf bukan kapital
                yi = ord(y) - 97 #agar nilai yi antara 0..25
                xi = D(ai,b,m,yi)
                x = xi + 97
        char = chr(x) #memunculkan karakter
    return char

def ciphered(password): #membuat chipered password
    chipered_password = ""
    for i in range (length(password)):
        char = encrypt(password[i])
        chipered_password+= char
    return chipered_password

def reverse_ciphered(chipered_password): #memanggil password asli
    password = ""
    for i in range(length(chipered_password)):
        char = decrypt(chipered_password[i])
        password+= char
    return password
