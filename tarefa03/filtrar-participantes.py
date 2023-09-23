
N, Q, V, M, a, b = input().split()

N = int(N)
Q = int(Q)
V = int(V)
M = float(M)

participantes = list()

for c in range(0, N):
    media = 0

    nome, leilao, win = input().split()
    
    leilao = int(leilao)
    
    win = int(win)
    
    if win > 0:
        for v in range(0, win):
            valor = float(input())
            media += valor
    
        media = media / win
    
    if leilao >= Q:
        participantes.append(nome)
    
    elif win >= V and media >= M:
        participantes.append(nome)
    
    elif nome[0] == a or nome [0] == b:
        participantes.append(nome)

for k in participantes:
    print(k)


