import os

#subistitua 'clear' por 'cls' para windows

tabuleiro = [ 
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "] 
            ]

def mostrar_tabuleiro():
    for i in range(3):
        print(tabuleiro[i][0], "|", tabuleiro[i][1], "|", tabuleiro[i][2])
        if i < 2:
            print("--+---+--")

def verificar_ganhador(tabuleiro):
    # verificar Linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ": #significa que -> X X X || O O O
            return True

    # verificar Colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            return True

    # verificar Diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return True

    return False

print("-----------------------------------")    
print("Bem vindo ao jogo da velha em python:")
print("\nJogo para 2 jogadores, em turnos.")
print("Cada jogador irá escolher linha e depois coluna onde jogará.")
print("Jogador 1 -> X | Jogador 2 -> O .")
print("-----------------------------------")

jogador1 =  str ( input("Dgitite seu nome jogador 1: ") )
jogador2 =  str ( input("Dgitite seu nome jogador 2: ") )

jogadas = 0

while True:

    jogada_ok = False
    while not jogada_ok:
        print("\nRodada de ", jogador1, "(X)")
        
        linha = int(input("Digite a linha (1-3): ")) - 1
        coluna = int(input("Digite a coluna (1-3): ")) - 1
        
        if  linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2:
            
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = "X"
                    jogada_ok = True
                    jogadas += 1
                    mostrar_tabuleiro()
                    
                else:
                    print("Posição ocupada!")
                    
        else:
            print("Linha ou coluna inválida! Escolha de 1 a 3.")
            
    vencedor = verificar_ganhador(tabuleiro)    
    if vencedor:    
        print("Parabéns", jogador1, "você ganhou!!")
        break   
    if jogadas == 9:
        print("Deu velha, ninguem ganhou :(")
        break
        
    jogada_ok = False
    
    while not jogada_ok: #enquanto não for True
        print("\nRodada de ", jogador2, "(O)")
        
        linha = int(input("Digite a linha (1-3): ")) - 1
        coluna = int(input("Digite a coluna (1-3): ")) - 1
        
        if  linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2:
            
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = "O"
                    jogada_ok = True
                    jogadas += 1
                    os.system('clear')
                    mostrar_tabuleiro()
                else:
                    os.system('clear')
                    print("Posição ocupada!")
                    
        else:
            print("Linha ou coluna inválida! Escolha de 1 a 3.")
        
    vencedor = verificar_ganhador(tabuleiro)    
    if vencedor:    
        print("Parabéns", jogador2, "você ganhou!!")
        break  
        