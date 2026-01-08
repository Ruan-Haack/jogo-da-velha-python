tabuleiro = [ 
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "] 
            ]


for i in range(3):
        print(tabuleiro[i][0], "|", tabuleiro[i][1], "|", tabuleiro[i][2])
        if i < 2:
            print("--+---+--")