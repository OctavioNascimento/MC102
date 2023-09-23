def sequencia(numero, contas):
    if numero == 1 or numero == 2 or numero == 3:
        return numero

    else:
        if numero in contas:
            return contas[numero]
        else:
            contas[numero] = (sequencia(numero-1, contas) + 2*sequencia(numero-2, contas) + 3*sequencia(numero-3, contas))
            return contas[numero]
            

def main():
    numero = int(input())
    contas = {}
    print(sequencia(numero, contas))
main()