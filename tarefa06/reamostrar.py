import math

def main():
    """
    chama o programa e verifica se as linhas tem o mesmo tamanho
    """
    matriz = []
    linhas = input()
    linhas = int(linhas)
    tamanho_linha = []

    for n in range(0, linhas):
        matriz.append(list(map(float, input().split())))

    for i in matriz:
        tamanho_linha.append(len(i))
    
    tamanho_linha.sort()

    if sum(tamanho_linha) / linhas == tamanho_linha[0]:
        print(" ".join(mesma_frequencia(matriz,linhas)))
    else: 
        matrizf = frequencias_multiplas(matriz,tamanho_linha)
        print(" ".join(mesma_frequencia(matrizf,linhas)))

    return

def mesma_frequencia(matriz,linhas):
    """
    soma as colunas
    """
    total = []
    for i in range(0, len(matriz[0])):
        soma = 0
        for j in range(0,linhas):
            soma += matriz[j][i]
        
        media = soma / linhas
        total.append(str(round(media, 2)))

    return total
    
def frequencias_multiplas(matriz,tamanho_linha):
    """
    normaliza as frequencias e identifica os intervalos
    """
    lista = []
    menor = tamanho_linha[0]

    for linhas in matriz:
        lista_linhas = []
        maior = len(linhas)
        if menor != 0:
            fracao = maior / menor 
        
        for c in range(0, menor):
            intervalo_menor = math.ceil(c * fracao)
            intervalor_maior = math.ceil((c + 1) * fracao)
            elemento = (linhas[intervalo_menor:intervalor_maior])
            if len(elemento) != 0:
                divisao = sum(elemento) / len(elemento)
                lista_linhas.append(divisao)

        lista.append(lista_linhas)

    return lista

main()

    



