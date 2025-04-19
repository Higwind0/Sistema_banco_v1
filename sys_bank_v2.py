# Defini uma classe {cliente} que armazena as variáveis do nosso sistema

class cliente:
    def __init__(self):
        self.saldo = 0
        self.extrato_cliente = []
        self.limite_diário = 1500
        self.saques_diários = 0
        self.usuarios = []
        self.contas = []
        self.contador_contas = 1

# A tela inicial que exibe as opções disponíveis na V1 do nosso projeto

    def menu(self):
        print(f"Olá, é muito bom te ver por aqui hoje!")
        print("Selecione umas das opções abaixo:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Cadastrar novo cliente")
        print("5 - Excluir Cliente")
        print("6 - Listar Clientes")
        print("7 - Cadastrar Conta Corrente")
        print("8 - Excluir Conta Corrente")
        print("9 - Listar Contas")
        print("10 - Sair")

# Regra para garantir que uma das opções disponíveis sejam digitada corretamente

        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
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
        elif deposito > 0:
            self.saldo += deposito
            self.extrato_cliente.append(
                f"Depósito: +R$ {deposito:.2f} efetuado por: {self.nome}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor não reconhecido! Digite um número válido.")
        self.menu_retorno()
        return

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
            elif saque <= 0:
                print("Por favor digite um valor maior do que zero!")
            else:
                self.saques_diários += 1
                self.saldo -= saque
                self.extrato_cliente.append(
                    f"Saque: -R$ {saque:.2f} efetuado por: {self.nome}")
                print("Saque realizado com sucesso!")
                self.menu_retorno()
                return

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
        return

# Método para sair do nosso sistema

    def sair(self):
        print("Até logo!")

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
                    opcao = self.menu()
                    self.executar_operacao(opcao)
                    break
                elif retorno == 2:
                    self.sair()
                    break
                else:
                    print("Por favor, digite 1 ou 2!")
            except ValueError:
                print("Comando não reconhecido! Digite um número válido.")

# Função adicionada na V2 - Cadastrar Cliente

    def cadastrar_cliente(self):
        cpf = input(f'Digite o CPF do cliente: ')
        if any(usuario["CPF"] == cpf for usuario in self.usuarios):
            print("CPF já cadastrado!")
            return

        nome = input(f'Digite o nome do cliente: ')
        data_nasc = input(f'Digite a Data de nascimento do cliente: ')
        endereco = input(f'Digite o Endereço do cliente: ')

        novo_usuario = {
            "CPF": cpf,
            "Nome": nome,
            "Data Nascimento": data_nasc,
            "Endereco": endereco
        }
        self.usuarios.append(novo_usuario)
        print("Conta Cadastrada com sucesso!")
        self.menu_retorno()
        return

# Função adicionada na V2 - Excluir Cliente

    def excluir_cliente(self):
        cpf = (input(f'Digite o CPF a ser Excluído: '))
        for usuario in self.usuarios:
            if usuario["CPF"] == cpf:
                self.usuarios.remove(usuario)
                print("Cliente excluído com Sucesso.")
                self.menu_retorno()
                return
        print("CPF não encontrado!")
        self.menu_retorno()
        return

# Função adicionada na V2 - Listar Clientes

    def listar_clientes(self):
        if not self.usuarios:
            print("Não existem usuários cadastrados")
            self.menu_retorno()
        else:
            print("\n--- LISTA DE CLIENTES ---")
            for usuario in self.usuarios:
                print(usuario)
        self.menu_retorno()
        return
        # Método que recebe a opção digitada e direciona para a operação correta

# Função adicionada na V2 - Cadastrar Conta

    def cadastrar_conta(self):
        numero_conta = self.contador_contas
        agencia = '0001'
        cpf = input("Digite o CPF do cliente: ")

        for usuario in self.usuarios:
            if usuario["CPF"] == cpf:
                nova_conta = {
                    "Agencia": agencia,
                    "Conta": numero_conta,
                    "Cliente": usuario["Nome"]
                }

                self.contas.append(nova_conta)
                self.contador_contas += 1
                print("Conta Cadastrada com Sucesso!")
                self.menu_retorno()
                return
        print("Para cadastrar uma conta, é necessário que o cliente esteja cadastrado!")
        self.menu_retorno()
        return


# Função adicionada na V2 - Excluir Conta

    def excluir_conta(self):
        deleta_conta = int(input(f'Digite a conta a ser Excluída: '))
        for numero_conta in self.contas:
            if numero_conta["Conta"] == deleta_conta:
                self.contas.remove(numero_conta)
                print("Conta excluída com Sucesso.")
                self.menu_retorno()
                return
        print("Conta não encontrada!")
        self.menu_retorno()
        return


# Função adicionada na V2 - Listar Contas


    def listar_contas(self):
        if not self.contas:
            print("Não existem contas cadastradas")
            self.menu_retorno()
        else:
            print("\n--- LISTA DE CONTAS ---")
            for conta in self.contas:
                print(conta)
        self.menu_retorno()
        return

    def executar_operacao(self, opcao):
        if opcao == 1:
            usuario.deposito()
        elif opcao == 2:
            usuario.saque()
        elif opcao == 3:
            usuario.exibir_extrato()
        elif opcao == 4:
            usuario.cadastrar_cliente()
        elif opcao == 5:
            usuario.excluir_cliente()
        elif opcao == 6:
            usuario.listar_clientes()
        elif opcao == 7:
            usuario.cadastrar_conta()
        elif opcao == 8:
            usuario.excluir_conta()
        elif opcao == 9:
            usuario.listar_contas()
        elif opcao == 10:
            usuario.sair()


# Criando a instância de cliente
# O nome "usuario" foi escolhido para evitar qualquer tipo de conflito com o nome da classe
usuario = cliente()

# Aqui chamamos/iniciamos a tela inicial do nosso sistema
opcao = usuario.menu()

# Aqui recebemos a opção-->(opcao) digitada e enviamos para o método "executar_operacao"
usuario.executar_operacao(opcao)


# ---- ALTERAÇÕES REALIZADAS PARA ATENDER A V2 DO SISTEMA ----
