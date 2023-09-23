def ordena(lista, maior):
    """
    Ordena 'lista' do maior para o menor, caso 'maior' seja True; caso
    contrário, ordena do menor para o maior. Essa função modifica a lista
    passada por parâmetro.

    Parâmetros: lista de números ou strings e um booleano.
    Retorna: nada.
    """    
    lista.sort(reverse = maior)

def moda(lista):
    """
    Encontra a moda de 'lista', isto é, o valor que mais se repete; em caso de
    empate, retorne o que aparece primeiro.

    Parâmetros: lista de strings.
    Retorna: a moda de 'lista'.
    """

    termo = 0
    moda = 0

    for i in lista:
        valor = 0
        for c in range(0, len(lista)):
            if i == lista[c]:
                valor += 1
        if termo < valor:
            moda = i
            termo = valor
    
    return moda

def mediana(valores):
    """
    Encontra a mediana de 'valores', isto é, o valor que ocupa a posição
    central da lista ordenada. Quando a lista tem tamanho par,
    definimos a mediana como o valor da primeira posição na segunda
    metada da lista ordenada.

    Parâmetros: lista de floats.
    Retorna: a mediana de 'valores'.
    """
    valores.sort()
    valor = (len(valores)/2)
    
    if valor == int(valor):
        mediana = valor

    else:       
        mediana = valor + 0.5
    
    return valores[int(mediana)]

def media(valores):
    """
    Encontra a média de 'valores'.

    Parâmetros: lista de floats.
    Retorna: a média de 'valores'.
    """

    soma = 0
    for i in valores:    
        soma += i
    return soma / len(valores)

def media_ponderada(valores, pesos):
    """
    Encontra a média ponderada de 'valores'.

    Parâmetros: listas de floats.
    Retorna: a média ponderada de 'valores'.
    """
    conte = valor = somp = 0
    while conte < len(valores):
        total = valores[conte] * pesos[conte]
        valor += total
        somp += pesos[conte]
        conte += 1

    valor /= somp
    
    return valor

def filtrar_entre(valores, menor, maior):
    """
    Cria uma lista com os números de 'valores' que estejam no intervalo
    ['menor', 'maior') (o primeiro intervalo é fechado e o segundo é aberto).

    Parâmetros: lista de floats e os limites.
    Retorna: a lista filtrada.
    """
    lista = []
    for i in valores:
        if i < menor or i >= maior:
            lista.append(i)
    for v in lista:
        valores.remove(v)
    return valores

def filtrar_caracteristica(lista, caracteristica, alvo):
    """
    Cria uma lista com os elementos de 'lista' cuja posição em 'caracteristica'
    seja igual a 'alvo'. Por exemplo, com a entrada abaixo, retornaríamos
    ['Alemanha', 'Portugal']:
    lista = ['Brasil', 'Alemanha', 'Angola', 'Portugal']
    caracteristica = ['América do Sul', 'Europa', 'África', 'Europa']
    alvo = 'Europa'

    Parâmetros: listas de números ou strings e um valor alvo.
    Retorna: a lista com a característica filtrada.
    """
    newlista = []
    while True:
        for c, i in enumerate(caracteristica):
            if i == alvo:
                newlista.append(lista[c])
        lista = newlista
        return lista
        break

def histograma(valores, intervalos):
    """
    Cria uma lista com as frequências do histograma de 'valores', divididas nas
    classes conforme a lista 'intervalos'. Por exemplo, se temos [10, 20, 30]
    como intervalos, devemos obter as frequências dos intervalos [10, 20) e [20,
    30).

    Parâmetros: listas de números.
    Retorna: lista de frequência do histograma.
    """
    histograma = []
    for i in range(0, (len(intervalos)-1)):
        cont = 0
        for a in valores:
            if intervalos[i] <= a < intervalos[i+1]:
                cont += 1
        histograma.append(cont)
    return histograma

def maiores_k(valores, k):
    """
    Cria uma lista com os 'k' maiores números de 'valores'.

    Parâmetros: lista de inteiros e um número inteiro.
    Retorna: lista com os 'k' maiores números.
    """
    valores.sort(reverse = True)
    lista_final = valores[0:k]
    return lista_final

def menores_k(valores, k):
    """
    Cria uma lista com os 'k' menores números de 'valores'.

    Parâmetros: lista de inteiros e um número inteiro.
    Retorna: lista com os 'k'menores números.
    """
    valores.sort()
    lista_final = valores[0:k]
    return lista_final

def remove_duplicatas(lista):
    """
    Cria uma lista removendo todos os elementos duplicados de 'lista', mantendo
    a ordem relativa original. Use somente listas, for/while e variáveis
    simples para implementar essa função.

    Parâmetros: listas de strings.
    Retorna: 'lista' sem duplicatas.
    """
    lista_final = []
    for i in lista:
        if i not in lista_final:
            lista_final.append(i)
    return lista_final