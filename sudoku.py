import copy

def selecionaGrade(num, lista_de_grade):
    """"Essa função exibe uma cópia de uma grade da lista sem alterar a grade original"""
    return copy.deepcopy(lista_de_grade[num -1])

def jogadaAtual(x, y, valor, grade, jogadas_possiveis):
    """Essa função realiza a jogada atual passando pela função de jogadas possíveis, caso não haja conflito o
       novo valor é inserido na grade e exibido. Caso haja conflito, exibe onde há o conflito."""
    x -= 1
    y -= 1
    coluna = []
    for i in range(len(grade)):
        coluna.append(grade[i][y])
    blocos = []
    for r in range(3):
        for c in range(3):
            bloco = []
            for i in range(3):
                for j in range(3):
                    bloco.append(grade[3*r+i][3*c+j])
            blocos.append(bloco)
    bloco_atual = blocos[x//3*3 + y//3]
    if (x, y) in jogadas_possiveis:
        if valor in grade[x]:
            print('Jogada na posição[%d,%d] inválida, este valor já está na linha'%(x+1, y+1))
        elif valor in coluna:
            print('Jogada na posição[%d,%d] inválida, este valor já está na coluna'%(x+1, y+1))
        elif valor in bloco_atual:
            print('Jogada na posição[%d,%d] inválida, este valor já está no bloco'%(x+1, y+1))
        else:
            grade[x][y] = valor
            return 1
    else:
        return 0
    return 0

def mostraGrade(grade):
    """Essa função exibe a grade"""
    for i in range(len(grade)):
        linha = '['
        for j in range(len(grade)):
            linha += str(grade[i][j])
            if j == len(grade) -1:
                linha += ']'
            else:
                linha += ' '
        print(linha)
    return


def jogadasPossiveis(grade):
    """Essa função verifica se a jogada é possível de ser feita sem conflitos"""
    jogadas_possiveis = []
    for i in range(len(grade)):
        for j in range(len(grade)):
            if grade[i][j] == 0:
                jogadas_possiveis.append((i,j))
    return jogadas_possiveis

def checaVitoria(grade):
    """Essa função checa se não há conflito em todos os blocos, linhas e colunas"""
    linhas = checaLinhas(grade)
    colunas = checaColunas(grade)
    blocos = checaBlocos(grade)
    vitoria = linhas + blocos + colunas
    return (vitoria == 3)


def checaLinhas(grade):
    """Essa função checa se existe conflito nas linhas"""
    for linha in grade:
        if len(set(linha)) != len(linha) or 0 in linha:
            return 0
    return 1

def checaColunas(grade):
    """Essa função checa se existe conflito nas colunas"""
    for i in range(len(grade)):
        coluna = []
        for j in range(len(grade)):
            coluna.append(grade[j][i])
        if len(set(coluna)) != len(grade) or 0 in coluna:
            return 0
    return 1

def checaBlocos(grade):
    """Essa função checa se existe conflito nos blocos"""
    for r in range(3):
        for c in range(3):
            bloco = []
            for i in range(3):
                for j in range(3):
                    bloco.append(grade[3*r+i][3*c+j])
            if len(set(bloco)) != len(grade) or 0 in bloco:
                return 0
    return 1

def main():
    #grade1
    grade1 = [[0,0,7,0,0,0,0,0,1], [0,0,0,0,6,0,3,8,5], [6,0,0,0,9,0,0,0,0], [0,9,0,0,0,0,0,0,0], [0,1,0,2,0,9,7,3,4], [0,5,3,1,0,4,2,6,9], [0,8,0,4,7,5,0,2,0], [0,7,0,0,1,0,0,0,3], [0,6,4,0,0,8,5,0,0]]

    #grade2
    grade2 = [[8,0,0,4,0,6,0,0,7], [0,0,0,0,0,0,4,0,0], [0,1,0,0,0,0,6,5,0], [5,0,9,0,3,0,7,8,0], [0,0,0,0,7,0,0,0,0], [0,4,8,0,2,0,1,0,3], [0,5,2,0,0,0,0,9,0], [0,0,1,0,0,0,0,0,0], [3,0,0,9,0,2,0,0,5]]

    #grade3
    grade3 = [[3,0,0,2,4,0,0,6,0], [0,4,0,0,0,0,0,5,3], [1,8,0,0,3,5,0,0,0], [0,0,0,0,8,0,2,0,0], [0,0,7,0,9,6,0,0,0], [8,0,0,1,0,0,0,0,0], [0,0,1,0,2,0,0,0,0], [2,0,0,3,0,0,7,4,0], [9,6,0,0,0,0,0,0,2]]

    #grade4
    grade4 = [[0,0,0,0,6,0,8,0,0], [7,0,3,0,0,0,2,0,0], [5,0,0,2,0,0,0,0,9], [8,0,5,0,0,6,0,0,2], [0,7,0,0,1,0,0,0,0], [4,0,0,9,0,0,0,0,5], [0,0,0,0,0,3,0,0,1], [0,0,4,0,0,0,5,0,0], [0,0,7,0,0,0,0,0,0]]

    #grade5
    grade5 = [[9,0,3,0,0,1,0,0,4], [0,1,0,7,0,3,0,0,0], [0,0,0,6,0,0,5,0,0], [0,0,0,0,8,0,0,0,7], [8,0,0,2,0,4,0,0,0], [2,0,0,0,6,0,0,0,0], [0,0,2,0,0,7,0,0,0], [3,0,0,0,0,2,0,6,0], [0,7,0,0,0,0,9,0,5]]
    
    lista_de_grade = [grade1, grade2, grade3, grade4, grade5]

    print('grade1')
    mostraGrade(grade1)
    print ('')
    print('grade2')
    mostraGrade(grade2)
    print ('')
    print('grade3')
    mostraGrade(grade3)
    print ('')
    print('grade4')
    mostraGrade(grade4)
    print ('')
    print('grade5')
    mostraGrade(grade5)
    grade_escolhida = int(input('Escolha com qual grade você quer jogar (apenas o número)'))
    grade = selecionaGrade(grade_escolhida, lista_de_grade)
    jogadas_possiveis = jogadasPossiveis(grade)

    while True:
        mostraGrade(grade)
        print('1. Fazer jogada')
        print('2. Resetar grade')
        print('3. Escolher nova grade')
        opcao = int(input(''))
        if opcao == 3:
            print('grade1')
            mostraGrade(grade1)
            print ('')
            print('grade2')
            mostraGrade(grade2)
            print ('')
            print('grade3')
            mostraGrade(grade3)
            print ('')
            print('grade4')
            mostraGrade(grade4)
            print ('')
            print('grade5')
            mostraGrade(grade5)
            grade_escolhida = int(input('Escolha com qual grade você quer jogar (apenas o número)'))
            grade = selecionaGrade(grade_escolhida, lista_de_grade)
            jogadas_possiveis = jogadasPossiveis(grade)
        elif opcao == 2:
            grade = selecionaGrade(grade_escolhida, lista_de_grade)
            jogadas_possiveis = jogadasPossiveis(grade)
        else:
            print('Escolha uma linha, uma coluna e um valor. (Ex: 1, 3, 8)')
            jogada = input('')
            jogada = jogada.split(', ')
            x = int(jogada[0])
            y = int(jogada[1])
            valor = int(jogada[2])
            possivel = jogadaAtual(x, y, valor, grade, jogadas_possiveis)
            if (possivel == 0):
                print('Jogada não permitida')
            if checaVitoria(grade):
                mostraGrade(grade)
                print('Parabéns! Você venceu.')
                return

main()
