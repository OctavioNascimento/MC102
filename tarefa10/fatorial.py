def fatorial(numero):
    if numero == 1 or numero == 0:
        return 1
    
    else:
        return numero*fatorial(numero-1)

def main():
    numero = int(input())
    print(fatorial(numero))
main()