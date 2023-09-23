def salvar(ents):
    """
    salva os valores dentro de moleculas
    """
    moleculas = set()
    for n in range(ents):
        numlist = input()
        moleculas.add(numlist)
    return moleculas

def encontrar(moleculas):
    """
    encontra e compara os elementos em moleculas com seus pares
    """
    usados = set()
    for elemento in moleculas:
        listatrio = set()
        elemento = set(elemento.split())
        for par2 in moleculas:
            par2 = set(par2.split())
            if len(par2 | elemento) == 3:
                novotrio = (par2 | elemento)
                novotrio = tuple(sorted(map(int,novotrio)))
                if novotrio not in listatrio:
                    listatrio.add(novotrio)
                else:
                    usados.add(novotrio)
                    moleculas = moleculas - elemento
    for tupla in sorted(usados):
        linha = f"{tupla[0]} {tupla[1]} {tupla[2]}"
        print(linha)

def main():
    ents = int(input())
    moleculas = salvar(ents)
    encontrar(moleculas)

main()