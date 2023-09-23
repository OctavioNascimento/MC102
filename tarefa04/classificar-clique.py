sites = []

qtde = int(input())
for c in range(0, qtde):
    nome = input()
    sites.append(nome)

valores = []

qtde = int(input())
for c in range(0, qtde):
    variaveis = []
    x0, y0, x1, y1, site = input().split()
    variaveis.append(int(x0))
    variaveis.append(int(x1))
    variaveis.append(int(y0))
    variaveis.append(int(y1))
    variaveis.append(site)
    valores.append(variaveis)

lista = []

while True:
    abajur = 0
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x == -1 and y == -1:
        break
    else:
        for i in valores:
            if (i[0] <= x) and (i[1] >= x) and (i[2] <= y) and (i[3] >= y):
                if i[4] in sites:
                    abajur = 1
                    break
                else:
                    abajur = 2
                    break
    if abajur == 1:
        print("malicioso")
    elif abajur == 2:
        print("seguro")
    else:
        print("nenhum")
        

        
            
