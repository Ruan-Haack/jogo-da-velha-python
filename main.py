import os
import random   

#subistitua 'clear' por 'cls' para windows

tabuleiro = [ 
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "] 
            ]

def mostrar_tabuleiro(tabuleiro):
    for i in range(3):
        print(tabuleiro[i][0], "|", tabuleiro[i][1], "|", tabuleiro[i][2])
        if i < 2:
            print("--+---+--")

def verificar_ganhador(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return tabuleiro[i][0]

    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            return tabuleiro[0][i]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]

    return None


def get_jogadas_possiveis(tabuleiro):
    jogadas = []

    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                jogadas.append((linha, coluna))

    return jogadas

def aplicar_jogada(tabuleiro, jogada, jogador):
    linha, coluna = jogada

    novo_tabuleiro = []
    for linha_tab in tabuleiro:
        novo_tabuleiro.append(linha_tab.copy())

    novo_tabuleiro[linha][coluna] = jogador
    mostrar_tabuleiro(novo_tabuleiro)
    print("\n")
    return novo_tabuleiro

def simulacao(tabuleiro_inicial, jogador_inicial):
    tabuleiro_copia = []
    for linha in tabuleiro_inicial:
        tabuleiro_copia.append(linha.copy())

    jogador = jogador_inicial

    while True:
        vencedor = verificar_ganhador(tabuleiro_copia)
        if vencedor:
            return vencedor
        
        jogadas = get_jogadas_possiveis(tabuleiro_copia)
        if not jogadas:
            return "Deu Velha #"

        jogada = random.choice(jogadas)
        tabuleiro_copia = aplicar_jogada(tabuleiro_copia, jogada, jogador)

        if jogador == "X":
            jogador = "O"    
        else:
            jogador = "X"

jogador = "X"
resultado = simulacao(tabuleiro, jogador)
print("Resultado da simulação:", resultado)
""" 
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
    
    if len(get_jogadas_possiveis(tabuleiro)) == 0:
        print("Deu velha, ninguém ganhou :(")
        break
    
    jogada_ok = False
    
    while not jogada_ok: #enquanto não for True
        print("\nRodada de ", jogador2, "(O)")
        
        print ("", get_jogadas_possiveis(tabuleiro))
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
        """