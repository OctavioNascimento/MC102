def maximo(entrada, verifica, maior):

    if verifica == len(entrada)-1:
        return maior

    else: 
        if entrada[verifica] > maior:
            maior = entrada[verifica]   
        verifica += 1
        return maximo(entrada, verifica, maior)


def main():  
    verifica = 0
    maior = 0
    entrada = list(map(int, input().split()))
    print(maximo(entrada, verifica, maior))
main()