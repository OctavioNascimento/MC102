def inicializar_contas():
    """
    Devolve um objeto representando o conjunto
    de contas bancárias inicialmente vazio.
    """
    contas = []
    return contas

def criar(contas, numero_conta):
    """
    Cria uma nova conta identificada por 'numero_conta' com
    saldo 0 e nenhuma movimentação associada.

    Devolve:
        - True se a conta tenha sido criada com sucesso
         -False se já existir conta com esse numero
    """
    usuarios = {

    "numero_conta":numero_conta,
    "saldo":0,
    } 

    for numero in contas:
        if numero_conta == numero["numero_conta"]:
            print("Esta conta já existe")
            return False

    contas.append(usuarios)

    return True
    
def movimentar(contas, numero_conta, data, valor, descricao, tipo):
    """
    Realiza uma movimentação na conta 'numero_conta'
    de valor 'valor' no dia 'data' descrita por 'descricao'.

    Devolve:
        - True se for possível realizar a movimentação
        - False caso contrário.
    """
    if tipo == "sacar":
        if float(valor) > consultar_saldo(contas, numero_conta):
            return False
        else:
            for i in contas:
                if numero_conta == i["numero_conta"]:
                    i["saldo"] -= float(valor)
            return True
    else:
        for i in contas:
            if (numero_conta) == (i["numero_conta"]):
                i["saldo"] += float(valor)
        return True

def consultar_saldo(contas, numero_conta):
    """
    Devolve o saldo da conta identificada por 'numero_conta'.
    """
    for i in contas:
        if numero_conta == i["numero_conta"]:
            saldo = i["saldo"]
            return saldo


