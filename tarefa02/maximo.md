a) maximo = inteiro
valor = inteiro

numero_digitado = inteiro
maximo = inteiro

b) lista = [1, -3, 4, 2, -5]
maximo = lista[0]
for valor in lista:      #neste caso for e in são iterações limitadas
    if valor > maximo:   #neste caso if é uma execução condicional
        maximo = valor
print(maximo)


numero_digitado = int(input())
maximo = numero_digitado
while numero_digitado >= 0:         #neste caso while iteração condicional
    if numero_digitado > maximo:    #neste caso if é execução condicional
        maximo = numero_digitado
    numero_digitado = int(input())
print(maximo)

Execução condicional: utilizadas quando uma função só pode ser executada caso alguma condição pré-definida seja verdadeira

Iteração condicional: utilizadas em situações onde uma repetição ocorre até sua condição for verdadeira

Iteração limitada: utilizadas em situações onde há uma quantidade de repetições pré-definidas

c) Daria para reescrever o primeiro algoritmo com while pois você consegue definir o limite da lista que será lida, colocando a condição para que a função vá até -5