def analise(demanda, disponiveis):
    """
    analisa e compara os valores das demandas e disponiveis
    """  
    restantes = []
    while True:
        if  len(demanda) == 0 or len(disponiveis) == 0:
            for num in demanda[:(len(demanda))]:
                restantes.append(num)
            break
        if disponiveis[0] == demanda[0]:
            del demanda[0]
            del disponiveis[0]
        elif disponiveis[0] > demanda[0]:
            restantes.append(demanda[0])
            del demanda[0]
        elif demanda[0] > disponiveis[0]:
            del disponiveis[0]
    print(" ".join(list(map(str, restantes))))

def main():
    demanda = input().split()
    disponivel = input().split()
    demanda = sorted(list(map(int, demanda)))
    disponivel = sorted(list(map(int, disponivel)))
    analise(demanda, disponivel)

main()