# biblioteca para limpar console
import os
# Variavel para o jogador decidir se vai jogar novamente
d = 0
# While para recomeçar o jogo enquanto d = 0
while d == 0:
    # matriz dos tabuleiros dos jogadores
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
    print("  1 2 3 4 5")
    for i in range(1, 6, 1):
        print(i, " ".join(matriz1[i - 1]))
    # armazenando nome, linha e coluna dos submarinos do primeiro jogador nas variaveis
    # logica do nome das variaveis: l11 = linha/jogador 1/submarino 1
    j1 = str(input("\nNome Jogador 1: "))
    l11 = int(input("Informe a linha do 1° submarino: "))
    c11 = int(input("Informe a coluna do 1° submarino: "))
    l12 = int(input("Informe a linha do 2° submarino: "))
    c12 = int(input("Informe a coluna do 2° submarino: "))
    l13 = int(input("Informe a linha do 3° submarino: "))
    c13 = int(input("Informe a coluna do 3° submarino: "))
    # clarear tela
    os.system("cls")
    # Entrada de dados do segundo jogador
    print("\nJogo Batalha Submarina\n")
    # exibição da matriz
    print("  1 2 3 4 5")
    for i in range(1, 6, 1):
        print(i, " ".join(matriz1[i - 1]))
    # armazenando nome, linha e coluna dos submarinos do segundo jogador
    # logica do nome das variaveis: l21 = linha/jogador 2/submarino 1
    j2 = str(input("\nNome Jogador 2: "))
    l21 = int(input("Informe a linha do 1° submarino: "))
    c21 = int(input("Informe a coluna do 1° submarino: "))
    l22 = int(input("Informe a linha do 2° submarino: "))
    c22 = int(input("Informe a coluna do 2° submarino: "))
    l23 = int(input("Informe a linha do 3° submarino: "))
    c23 = int(input("Informe a coluna do 3° submarino: "))
    # while para que o jogo continue até um dos jogadores acertar os 3 submarinos do adversário
    while a1 != 3 or a2 != 3:
        os.system("cls")
        # jogador 1 iniciando com enter
        print("Jogador 1 ", j1,", pressione ENTER para continuar!")
        input()
        os.system("cls")
        # Vez do Jogador 1
        print("Jogador 1: ", j1, "\nTiros: ", t1, " Acertos: ", a1, "\n")
        # exibição da matriz
        print("  1 2 3 4 5")
        for i in range(1, 6, 1):
            print(i, " ".join(matriz1[i - 1]))
        # Tentativa do jogador 1
        l = int(input("\nQual linha? "))
        c = int(input("Qual coluna? "))
        # Verificando se o jogador está repetindo o tiro
        while matriz1[l - 1][c - 1] == 'X' or matriz1[l - 1][c - 1] == 'S':
            print("\nVocê já atirou nessa linha e coluna! Informe uma posição diferente para seguir o jogo.")
            # entrada da nova posição
            l = int(input("\nQual linha? "))
            c = int(input("Qual coluna? "))
        # Comparando tentativa do jogador com as variaveis armazenadas dos submarinos do segundo jogador
        if l == l21 and c == c21:
            # contador de acertos
            a1 += 1
            matriz1[l - 1][c - 1] = 'S'
            os.system("cls")
            print("Jogador 1: ", j1, "\nTiros: ", t1 + 1, " Acertos: ", a1, "\n")
            # exibição da matriz
            print("  1 2 3 4 5")
            for i in range(1, 6, 1):
                print(i, " ".join(matriz1[i - 1]))
            print("\nACERTOU!")
        elif l == l22 and c == c22:
            # contador de acertos
            a1 += 1
            matriz1[l - 1][c - 1] = 'S'
            os.system("cls")
            print("Jogador 1: ", j1, "\nTiros: ", t1 + 1, " Acertos: ", a1, "\n")
            # exibição da matriz
            print("  1 2 3 4 5")
            for i in range(1, 6, 1):
                print(i, " ".join(matriz1[i - 1]))
            print("\nACERTOU!")
        elif l == l23 and c == c23:
            # contador de acertos
            a1 += 1
            matriz1[l - 1][c - 1] = 'S'
            os.system("cls")
            print("Jogador 1: ", j1, "\nTiros: ", t1 + 1, " Acertos: ", a1, "\n")
            # exibição da matriz
            print("  1 2 3 4 5")
            for i in range(1, 6, 1):
                print(i, " ".join(matriz1[i - 1]))
            print("\nACERTOU!")
        else:
            matriz1[l - 1][c - 1] = 'X'
            os.system("cls")
            print("Jogador 1: ", j1, "\nTiros: ", t1 + 1, " Acertos: ", a1, "\n")
            # exibição da matriz
            print("  1 2 3 4 5")
            for i in range(1, 6, 1):
                print(i, " ".join(matriz1[i - 1]))
            print("\nERROU!")
        input()
        # Verificando se o jogador 1 atingiu os 3 acertos, caso seja true, encerra o while
        if a1 == 3:
            os.system("cls")
            print("Jogador 1: ", j1, " é o vencedor!\n")
            break
        os.system("cls")
        # jogador 2 iniciando com enter
        print("Jogador 2 ", j2, ", pressione ENTER para continuar!")
        input()
        os.system("cls")
        # Vez do Jogador 2
        print("Jogador 2: ", j2, "\nTiros: ", t2, " Acertos: ", a2, "\n")
        # exibição da matriz
        print("  1 2 3 4 5")
        for i in range(1, 6, 1):
            print(i, " ".join(matriz2[i - 1]))
        # Tentativa do jogador 2
        l = int(input("\nQual linha? "))
        c = int(input("Qual coluna? "))
        # Verificando se o jogador está repetindo o tiro
        while matriz1[l - 1][c - 1] == 'X' or matriz1[l - 1][c - 1] == 'S':
            print("\nVocê já atirou nessa linha e coluna! Informe uma posição diferente para seguir o jogo.")
            # entrada da nova posição
            l = int(input("\nQual linha? "))
            c = int(input("Qual coluna? "))
        # Comparando tentativa do jogador com as variaveis armazenadas dos submarinos do segundo jogador
        if l == l11 and c == c11:
            # contador de acertos
            a2 += 1
            matriz2[l - 1][c - 1] = 'S'
            os.system("cls")
            print("Jogador 2: ", j2, "\nTiros: ", t2 + 1, " Acertos: ", a2, "\n")
            # exibição da matriz
            print("  1 2 3 4 5")
            for i in range(1, 6, 1):
                print(i, " ".join(matriz2[i - 1]))
            print("\nACERTOU!")
        elif l == l12 and c == c12:
            # contador de acertos
            a2 += 1
            matriz2[l - 1][c - 1] = 'S'
            os.system("cls")
            print("Jogador 2: ", j2, "\nTiros: ", t2 + 1, " Acertos: ", a2, "\n")
            # exibição da matriz
            print("  1 2 3 4 5")
            for i in range(1, 6, 1):
                print(i, " ".join(matriz2[i - 1]))
            print("\nACERTOU!")
        elif l == l13 and c == c13:
            # contador de acertos
            a2 += 1
            matriz2[l - 1][c - 1] = 'S'
            os.system("cls")
            print("Jogador 2: ", j2, "\nTiros: ", t2 + 1, " Acertos: ", a2, "\n")
            # exibição da matriz
            print("  1 2 3 4 5")
            for i in range(1, 6, 1):
                print(i, " ".join(matriz2[i - 1]))
            print("\nACERTOU!")
        else:
            matriz2[l - 1][c - 1] = 'X'
            os.system("cls")
            print("Jogador 2: ", j2, "\nTiros: ", t2 + 1, " Acertos: ", a2, "\n")
            # exibição da matriz
            print("  1 2 3 4 5")
            for i in range(1, 6, 1):
                print(i, " ".join(matriz2[i - 1]))
            print("\nERROU!")
        input()
        # Verificando se o jogador 1 atingiu os 3 acertos, caso seja true, encerra o while
        if a2 == 3:
            os.system("cls")
            print("Jogador 2: ", j2, " é o vencedor!\n")
            break
        # contador de tiros de cada jogador
        t1 += 1
        t2 += 1
    # Verificando se o jogador quer reiniciar o jogo
    d = int(input("Digite 0 se quiser jogar novamente ou digite 1 para encerrar o jogo: "))
    os.system("cls")
print("Fim de jogo!")
