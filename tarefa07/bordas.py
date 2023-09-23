import sys

import testes

def carregar_imagem(entrada):
    """
Carrega um arquivo de imagem de um repositório para o programa
"""
    with open(entrada) as arquivo:
        img_lista = []
        for linha in arquivo:
            img_lista.append(linha.split())
    
    return img_lista

def identificar_pixel(matriz, dimensao):
    """
Identifica se o pixel é preto ou branco na imagem
"""
    formatriz = []
    for linha in range(int(dimensao[1])):
        linhas = []
        for termo in range(int(dimensao[0])):
            if matriz[linha][termo] == "1":
                linhas.append(identificar_bordas(linha, termo, matriz))
            else: 
                linhas.append("0")
        formatriz.append(linhas)
    return formatriz
                

def identificar_bordas(linha, termo, matriz):
    for i in range(3):
        for j in range(3):
            if matriz[i+linha-1][j+termo-1] == "0":
                return "1"

    return "0"        

def criar_arquivo(saida, matriz):
    with open(saida,"w") as arquivo:
        for linha in matriz:
            print(" ".join(linha),file=arquivo)

def main():
    entrada = sys.argv[1]
    saida = sys.argv[2]
    matriz = carregar_imagem(entrada)
    dimensao = matriz[1]
    del matriz[0:2]
    formatriz = identificar_pixel(matriz, dimensao)
    formatriz.insert(0,["P1"])
    formatriz.insert(1,dimensao)
    criar_arquivo(saida, formatriz)
main ()