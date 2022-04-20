from modul.pecah import*
import datetime

quotes_kerang_ajaib = ["Ya","Tidak",
    "Bisa Jadi",
    "Mungkin",
    "Tentunya",
    "Tidak Mungkin",
    "Coba pikirkan sendiri",
    "UWOOOOOOOOOOOOOOOGHH YES OFC",
    "pake nanya lg u",
    "wut u say",
    "yes ofc",
    "no!!!",
    "yes!!!!",
    "yes???",
    "lol literally no",
    "honestly I don't care lol",
    "kgk lah parbet si u",
    "auk dah",
    "tanyakan pada rumput yang bergoyang~",
    "NO!!!!!!!!!",
    "Coba tanya pendapat Lesti!",
    "404 not found",
    "Entahlah",
    "Y",
    "G",
    "trsrh",
    "sabebb",
    "kuyyy",
    "kerang lagi tidur",
    "sumbarang ang lah",
    "tu baa?",
    "awak tanyo ka gaek lu",
    "cek kerang sebelah",
    "tanya bapak kao la",
    "wes turu aku ms",
    "masa gitu aj gk tau:/",
    "yoi maszehhhh",
    "oi Kiyomasa, nande..nande",
    "Baka",
    "Kimochi Warui",
    "Kawaii",
    "o kawai koto",
    "ohayou onii-chan > /// <",
    "Nico nico nii <3",
    "Dattebayo",
    "kaizoku ou ni, ore wa naru!",
    "Oodama rasengan",
    "Dame dane",
    "Dame yo",
    "Dame nano yo",
    "ora ora ora ora",
    "URRRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "apa coba????",
    "Paansihhh",
    "sekut atuh mang",
    "ok.",
    "Gitu aja kok repot",
    "YNTKTS",
    "hiya",
    "p mksd",
    "good enough",
    "you wish",
    "whatever, who cares",
    "GPP"    
    ]
def LCG(x):
    a = 11
    c = 13
    m = length(quotes_kerang_ajaib)
    indeks = ((a*x)+c)%m
    return indeks

def kerangajaib():
    question = input("Apa pertanyaanmu? ")
    now = datetime.datetime.now()
    x = int(now.second) + int(now.minute) + int(now.hour) #ambil waktu
    indeks = LCG(x)
    print()
    print(quotes_kerang_ajaib[indeks])

