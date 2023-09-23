import contas

def main():
    conta = contas.inicializar_contas()
    
    while True:
        
        entrada = input()
        
        if entrada == "abrir":
            numero_conta = (input())
            contas.criar(conta, numero_conta)
            print("Conta aberta com sucesso")
        
        elif entrada == "saldo":
            numero_conta = (input())
            saldo = contas.consultar_saldo(conta, numero_conta)
            print(f"O saldo da conta é R$ {saldo:.2f}")
        
        elif entrada == "depositar":
            numero_conta, valor, data, descricao = input().split(maxsplit=3)
            contas.movimentar(conta, numero_conta, data, valor, descricao, entrada)
            print("Depósito realizado com sucesso")

        elif entrada == "sacar":
            numero_conta, valor, data, descricao = input().split(maxsplit=3)
            contas.movimentar(conta, numero_conta, data, valor, descricao, entrada)
            print("Saque realizado com sucesso")
        
        elif entrada == "sair":
            break
main()


