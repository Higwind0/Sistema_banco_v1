# Defini uma classe {cliente} que armazena as variáveis do nosso sistema

class cliente:
    def __init__(self):
        self.nome = "Sargento"
        self.saldo = 0
        self.extrato_cliente = []
        self.limite_diário = 1500
        self.saques_diários = 0

# A tela inicial que exibe as opções disponíveis na V1 do nosso projeto

    def tela_inicial(self):
        print(f"Olá {self.nome}, é muito bom te ver por aqui hoje!")
        print("Selecione umas das opções abaixo:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Sair")

# Regra para garantir que uma das opções disponíveis seja digitada corretamente

        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao in [1, 2, 3, 4]:
                    return opcao
                else:
                    print("Por favor, digite uma opção entre 1 e 4!")
            except ValueError:
                print("Comando não reconhecido!")

# Definição da regra de depósito, adicionei uma regra para não aceitar valores menores ou iguais a 0

    def deposito(self):
        print(f"Digite o valor que deseja depositar:")
        deposito = int(input("R$ "))
        if deposito <= 0:
            print("Digite um valor superior a 0")
        elif deposito >0:
            self.saldo += deposito
            self.extrato_cliente.append(f"Depósito: +R$ {deposito:.2f} efetuado por: {self.nome}")
            print("Depósito realizado com sucesso!")                   
        else:
            print("Valor não reconhecido! Digite um número válido.")
        self.menu_retorno()

# Definição da regra de saque, garantindo as regras referente a limites diários, saldo e valor maior que 0

    def saque(self):
        if self.saldo <= 0:
            print("Saldo insuficiente para realizar saque!")
            self.menu_retorno()
        elif self.saques_diários >= 3:
            print("Limite de saques diários atingido!")
            self.menu_retorno()
        else:
            print(f"Digite o valor que deseja sacar:")
            saque = int(input("R$ "))
            if saque > 500:
                print("Limite de saque por operação é de R$ 500,00!")
                self.menu_retorno()
            elif saque <=0:
                print("Por favor digite um valor maior do que zero!")
            else:
                self.saques_diários += 1
                self.saldo -= saque
                self.extrato_cliente.append(f"Saque: -R$ {saque:.2f} efetuado por: {self.nome}")
                print("Saque realizado com sucesso!")
                self.menu_retorno()

# Exibir extrato, adicinoei regra para exibir apenas quando houver movimentação, no final do extrato exibe o saldo atual

    def exibir_extrato(self):
        print("\n=== EXTRATO ===")
        if not self.extrato_cliente:
            print("Nenhuma operação registrada.")
        else:
            for item in self.extrato_cliente:
                print(item)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        self.menu_retorno()

# Método para sair do nosso sistema

    def sair(self):
        print("Até mais, Sargento!")

# Criei um menu de retorno para dar fluidez ao navegar nas opções.
# Foi adicionada opção "self.menu_retorno()" em cada operação
# Também foi garantido que o usuário digite uma opção válida

    def menu_retorno(self):
        while True:
            print("Deseja realizar mais alguma operação?")
            print("1 - Sim")
            print("2 - Não")
            
            try:
                retorno = int(input("Escolha uma opção: "))
                if retorno == 1:
                    opcao = self.tela_inicial()
                    self.executar_operacao(opcao)
                    break
                elif retorno == 2:
                    self.sair()
                    break
                else:
                    print("Por favor, digite 1 ou 2!")
            except ValueError:
                print("Comando não reconhecido! Digite um número válido.")

# Método que recebe a opção digitada e direciona para a operação correta 

    def executar_operacao(self, opcao):
        if opcao == 1:
            usuario.deposito()
        elif opcao == 2:
            usuario.saque()
        elif opcao == 3:
            usuario.exibir_extrato()
        elif opcao == 4:
            usuario.sair()


# Criando a instância de cliente
# O nome "usuario" foi escolhido para evitar qualquer tipo de conflito com o nome da classe

usuario = cliente()

# Aqui chamamos/iniciamos a tela inicial do nosso sistema
opcao = usuario.tela_inicial()

# Aqui recebemos a opção-->(opcao) digitada e enviamos para o método "executar_operacao"
usuario.executar_operacao(opcao)

