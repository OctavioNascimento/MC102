
comando = (input())

codigo_produto = 0

lance_minimo = 0.0

if comando == "I":
    codigo_produto, lance_minimo = input().split()
    print(f"Bem-vindo ao Leilão de Algoritmópolis! Produto {codigo_produto} com lance mínimo R$ {lance_minimo}")

codigo_produto = int(codigo_produto)

lance_minimo = float(lance_minimo)

lance_maximo = 0.0
    
numero_lances = 0

comando = (input())

while comando != "F":

    if comando == "L":
        nome, valor_lance = input().split()
        valor_lance = float(valor_lance)
        if valor_lance >= lance_minimo and valor_lance > lance_maximo:
            print(f"{nome} deu um lance de R$ {valor_lance:.2f}")
            lance_maximo = valor_lance
            numero_lances += 1
            nome_vencedor = nome
        else:
            print(f"Lance inválido de {nome}")

    if comando == "S":
        print(f"Status do Leilão do Produto {codigo_produto}")
        if numero_lances >= 1:
            print(f"{numero_lances} lances até agora")
            print(f"{nome_vencedor} deu o melhor lance, de valor R$ {lance_maximo:.2f}")
        else: print("Não houve lances")
        

    comando = (input())

if comando == "F":
    print(f"Leilão finalizado com {numero_lances} lances")
    print(f"{nome_vencedor} venceu com o lance de valor R$ {lance_maximo:.2f}")
    if float(valor_lance) <= lance_minimo:
        print("Não houve vencedor")