
nome = input("Qual o seu nome: ")

participacao_leiloes = int(input("Quantos leilões já participou antes: "))

lances_vencidos = int(input("Quantos lances você já venceu: "))

if(lances_vencidos >= 2):
    l1 = float(input("Lance vencedor 1: "))
    l2 = float(input("Lance vencedor 2: "))
    if (l1 + l2) / 2 >= 120.45:
        print("Parabéns! Você pode se inscrever.")

    elif (nome[0] == 'D' or nome[0] == 'R'):
        print("Parabéns! Você pode se inscrever.")

elif (nome[0] == 'D' or nome[0] == 'R'):
        print("Parabéns! Você pode se inscrever.")

elif (participacao_leiloes >= 3):
    print("Parabéns! Você pode se inscrever.")

else: 
    print("Infelizmente, você não poderá participar nesse ano.")