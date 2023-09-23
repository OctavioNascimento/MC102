import sys
import modulo_analise as m

def main():
    acao = sys.argv[1]
    if acao == "produtividade":
        ano1, ano2 = input().split()
        produtividade(ano1, ano2)

    return

indices = []
paises = []
anos = []
classes = []
duracoes = []

with open("testes/filmes.dat") as f:
    for linha in f:
        indice, pais, ano, classe, duracao = linha.split()
        indices.append(int(indice))
        paises.append(pais)
        anos.append(int(ano))
        classes.append(classe)
        duracoes.append(int(duracao))

def produtividade(ano1, ano2):

    quantidade = 0

    for i in range(int(ano1), int(ano2) + 1):
        for c in range(len(anos)):
            if i == anos[c]:
                quantidade += 1
        print(f"{i}: {quantidade}")
        quantidade = 0

    return

main()