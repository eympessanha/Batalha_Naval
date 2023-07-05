import os
def repTiro(matriz1,l,c):
    if matriz1[l - 1][c - 1] == 'X' or matriz1[l - 1][c - 1] == 'S':
        print("Tiro repetido! Informe uma posição diferente.")
        return True
def posiRep(l11,c11,l12,c12):
    if l11==l12 and c11==c12:
        print("Já existe um submarino nessa posição! Informe uma posição diferente.")
        return True
def foraMatriz(l11,c11):
    if l11>5 or l11<1 or c11>5 or c11<1:
        print("Submarino fora do tabuleiro! Informe outra posição.")
        return True
def apagarTela():
    os.system("cls")
def exibirMatriz(matriz1):
    print("  1 2 3 4 5")
    for i in range(1, 6, 1):
        print(i, " ".join(matriz1[i - 1]))

# Variavel para o jogador decidir se vai jogar novamente
d = 0

while d == 0:
    matriz1 = []
    matriz2 = []
    # acertos, tiros e linha e coluna que cada jogador coloca durante o jogo
    a1 = 0
    a2 = 0
    t1 = 0
    t2 = 0
    l = 0
    c = 0
    # iniciando jogo
    print("\nJogo Batalha Submarina\n")
    # criação das matrizes
    for i in range(1, 6, 1):
        linha1 = []
        linha2 = []
        for j in range(1, 6, 1):
            linha1.append('o')
            linha2.append('o')
        matriz1.append(linha1)
        matriz2.append(linha2)
    # exibição da matriz
    exibirMatriz(matriz1)
    # armazenando nome, linha e coluna dos submarinos do primeiro jogador nas variaveis
    # logica do nome das variaveis: l11 = linha/jogador 1/submarino 1
    j1 = str(input("\nNome Jogador 1: "))
    l11 = int(input("Informe a linha do 1° submarino: "))
    c11 = int(input("Informe a coluna do 1° submarino: "))
    while foraMatriz(l11,c11) == True:
        l11 = int(input("Informe a linha do 1° submarino: "))
        c11 = int(input("Informe a coluna do 1° submarino: "))
    l12 = int(input("Informe a linha do 2° submarino: "))
    c12 = int(input("Informe a coluna do 2° submarino: "))
    while posiRep(l11, c11, l12, c12) == True:
        l12 = int(input("Informe a linha do 2° submarino: "))
        c12 = int(input("Informe a coluna do 2° submarino: "))
    while foraMatriz(l12, c12) == True:
        l12 = int(input("Informe a linha do 2° submarino: "))
        c12 = int(input("Informe a coluna do 2° submarino: "))
    l13 = int(input("Informe a linha do 3° submarino: "))
    c13 = int(input("Informe a coluna do 3° submarino: "))
    while posiRep(l11, c11, l13, c13) == True or posiRep(l13, c13, l12, c12) == True:
        l13 = int(input("Informe a linha do 3° submarino: "))
        c13 = int(input("Informe a coluna do 3° submarino: "))
    while foraMatriz(l13, c13) == True:
        l13 = int(input("Informe a linha do 3° submarino: "))
        c13 = int(input("Informe a coluna do 3° submarino: "))
    # clarear tela
    apagarTela()

    # Entrada de dados do segundo jogador
    print("\nJogo Batalha Submarina\n")
    # exibição da matriz
    exibirMatriz(matriz1)
    # armazenando nome, linha e coluna dos submarinos do segundo jogador
    # logica do nome das variaveis: l21 = linha/jogador 2/submarino 1
    j2 = str(input("\nNome Jogador 2: "))
    l21 = int(input("Informe a linha do 1° submarino: "))
    c21 = int(input("Informe a coluna do 1° submarino: "))
    while foraMatriz(l21, c21) == True:
        l21 = int(input("Informe a linha do 1° submarino: "))
        c21 = int(input("Informe a coluna do 1° submarino: "))
    l22 = int(input("Informe a linha do 2° submarino: "))
    c22 = int(input("Informe a coluna do 2° submarino: "))
    while posiRep(l21, c21, l22, c22) == True:
        l22 = int(input("Informe a linha do 2° submarino: "))
        c22 = int(input("Informe a coluna do 2° submarino: "))
    while foraMatriz(l22, c22) == True:
        l22 = int(input("Informe a linha do 2° submarino: "))
        c22 = int(input("Informe a coluna do 2° submarino: "))
    l23 = int(input("Informe a linha do 3° submarino: "))
    c23 = int(input("Informe a coluna do 3° submarino: "))
    while posiRep(l21, c21, l23, c23) == True or posiRep(l23, c23, l22, c22) == True:
        l23 = int(input("Informe a linha do 3° submarino: "))
        c23 = int(input("Informe a coluna do 3° submarino: "))
    while foraMatriz(l23, c23) == True:
        l23 = int(input("Informe a linha do 3° submarino: "))
        c23 = int(input("Informe a coluna do 3° submarino: "))

    # while para que o jogo continue até um dos jogadores acertar os 3 submarinos do adversário
    while a1 != 3 or a2 != 3:
        apagarTela()
        # jogador 1 iniciando com enter
        print("Jogador 1 ", j1,", pressione ENTER para continuar!")
        input()
        apagarTela()
        # Vez do Jogador 1
        print("Jogador 1: ", j1, "\nTiros: ", t1, " Acertos: ", a1, "\n")
        exibirMatriz(matriz1)
        # Tentativa do jogador 1
        l = int(input("\nQual linha? "))
        c = int(input("Qual coluna? "))
        while foraMatriz(l,c) == True:
            l = int(input("\nQual linha? "))
            c = int(input("Qual coluna? "))
            while repTiro(matriz1, l, c) == True:
                l = int(input("\nQual linha? "))
                c = int(input("Qual coluna? "))
        # Verificando se o jogador está repetindo o tiro
        while repTiro(matriz1,l,c) == True:
            l = int(input("\nQual linha? "))
            c = int(input("Qual coluna? "))
            while foraMatriz(l, c) == True:
                l = int(input("\nQual linha? "))
                c = int(input("Qual coluna? "))
        # Comparando tentativa do jogador com as variaveis armazenadas dos submarinos do segundo jogador
        if l == l21 and c == c21:
            # contador de acertos
            a1 += 1
            matriz1[l - 1][c - 1] = 'S'
            apagarTela()
            print("Jogador 1: ", j1, "\nTiros: ", t1 + 1, " Acertos: ", a1, "\n")
            # exibição da matriz
            exibirMatriz(matriz1)
            print("\nACERTOU!")
        elif l == l22 and c == c22:
            # contador de acertos
            a1 += 1
            matriz1[l - 1][c - 1] = 'S'
            apagarTela()
            print("Jogador 1: ", j1, "\nTiros: ", t1 + 1, " Acertos: ", a1, "\n")
            # exibição da matriz
            exibirMatriz(matriz1)
            print("\nACERTOU!")
        elif l == l23 and c == c23:
            # contador de acertos
            a1 += 1
            matriz1[l - 1][c - 1] = 'S'
            apagarTela()
            print("Jogador 1: ", j1, "\nTiros: ", t1 + 1, " Acertos: ", a1, "\n")
            # exibição da matriz
            exibirMatriz(matriz1)
            print("\nACERTOU!")
        else:
            matriz1[l - 1][c - 1] = 'X'
            apagarTela()
            print(l,c)
            print("Jogador 1: ", j1, "\nTiros: ", t1 + 1, " Acertos: ", a1, "\n")
            # exibição da matriz
            exibirMatriz(matriz1)
            print("\nERROU!")
        input()
        # Verificando se o jogador 1 atingiu os 3 acertos, caso seja true, encerra o while
        if a1 == 3:
            apagarTela()
            print("Jogador 1: ", j1, " é o vencedor!\n")
            break
        apagarTela()
        # jogador 2 iniciando com enter
        print("Jogador 2 ", j2, ", pressione ENTER para continuar!")
        input()
        apagarTela()
        # Vez do Jogador 2
        print("Jogador 2: ", j2, "\nTiros: ", t2, " Acertos: ", a2, "\n")
        # exibição da matriz
        exibirMatriz(matriz2)
        # Tentativa do jogador 2
        l = int(input("\nQual linha? "))
        c = int(input("Qual coluna? "))
        while foraMatriz(l,c) == True:
            l = int(input("\nQual linha? "))
            c = int(input("Qual coluna? "))
            while repTiro(matriz2, l, c) == True:
                l = int(input("\nQual linha? "))
                c = int(input("Qual coluna? "))
        # Verificando se o jogador está repetindo o tiro
        while repTiro(matriz2,l,c) == True:
            l = int(input("\nQual linha? "))
            c = int(input("Qual coluna? "))
            while foraMatriz(l, c) == True:
                l = int(input("\nQual linha? "))
                c = int(input("Qual coluna? "))
        # Comparando tentativa do jogador com as variaveis armazenadas dos submarinos do segundo jogador
        if l == l11 and c == c11:
            # contador de acertos
            a2 += 1
            matriz2[l - 1][c - 1] = 'S'
            apagarTela()
            print("Jogador 2: ", j2, "\nTiros: ", t2 + 1, " Acertos: ", a2, "\n")
            # exibição da matriz
            exibirMatriz(matriz2)
            print("\nACERTOU!")
        elif l == l12 and c == c12:
            # contador de acertos
            a2 += 1
            matriz2[l - 1][c - 1] = 'S'
            apagarTela()
            print("Jogador 2: ", j2, "\nTiros: ", t2 + 1, " Acertos: ", a2, "\n")
            # exibição da matriz
            exibirMatriz(matriz2)
            print("\nACERTOU!")
        elif l == l13 and c == c13:
            # contador de acertos
            a2 += 1
            matriz2[l - 1][c - 1] = 'S'
            apagarTela()
            print("Jogador 2: ", j2, "\nTiros: ", t2 + 1, " Acertos: ", a2, "\n")
            # exibição da matriz
            exibirMatriz(matriz2)
            print("\nACERTOU!")
        else:
            matriz2[l - 1][c - 1] = 'X'
            apagarTela()
            print("Jogador 2: ", j2, "\nTiros: ", t2 + 1, " Acertos: ", a2, "\n")
            # exibição da matriz
            exibirMatriz(matriz2)
            print("\nERROU!")
        input()
        # Verificando se o jogador 1 atingiu os 3 acertos, caso seja true, encerra o while
        if a2 == 3:
            apagarTela()
            print("Jogador 2: ", j2, " é o vencedor!\n")
            break
        # contador de tiros de cada jogador
        t1 += 1
        t2 += 1
    # Verificando se o jogador quer reiniciar o jogo
    d = int(input("Digite 0 se quiser jogar novamente ou digite 1 para encerrar o jogo: "))
    apagarTela()
print("Fim de jogo!")
