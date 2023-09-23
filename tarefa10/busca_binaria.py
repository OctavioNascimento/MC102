def busca_binaria(entrada, valor, pmin, pmax):
    if pmin == pmax: 
        return pmin
    else:
        metade_lista = (pmax + pmin) // 2
    
        if valor > entrada[metade_lista]:
            return busca_binaria(entrada, valor, metade_lista + 1, pmax)
    
        else:
            return busca_binaria(entrada, valor, pmin,metade_lista)

def main():
    pmin = 0
    entrada = list(map(int, input().split()))
    pmax = len(entrada)-1
    valor = int(input())
    posicao = busca_binaria(entrada, valor, pmin, pmax)
    if entrada[posicao] == valor:
        print(posicao)
    else:
        print(-1)
main()