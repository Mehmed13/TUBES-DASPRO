"""def strip_line(baris):
    for i, c in enumerate(baris):
        if not c.isspace():
            return baris[i:]
"""

print(">>> buy_game")

IDGame = input("Masukkan ID Game: ")

baca = open("game.csv", "r")
listgame = baca.readlines()
    