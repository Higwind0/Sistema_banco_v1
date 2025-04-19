<h1 align=center>Banking System</h4>


🎯Criar um sistema bancário de acordo com as seguintes especificações:
## Depósito
```yaml
1. Apenas deve ser possível depositar valores positivos
2. Os depósitos devem ser armazenados em uma variável para consulta de extato
3. Não deve ser possível depositar valores não inteiros
```

## Saque
```yaml
1. Deve ser possível realizar no máximo 3 saques diários
2. O valor máximo de cada saque deve ser de R$500 reais
3. Caso não houver saldo o sistema deve exibir mensagem de erro "Sem saldo"
4. Os saques devem ser armazenados em uma variável para consulta de extato
```

## Extrato
```yaml
1. Deve listar todos os depósitos e saques realizados na conta.
2. Ao final da listagem do extrato deve ser exibido o SALDO atual.
3. O formato a ser exibido deve ser R$ XXX.XX
```
<h1 align=center>Alterações v1</h4>
Arquivo criado em 26/03/2025
<h4>As seguintes alterações foram realizadas por falta de especificação do sistema para melhorar a usabilidade:</h4>


1. Criado um método de retorno para navegação entre os itens. Necessário, pois, caso não houver, o código vai encerrar após cada ação realizada. Dessa forma se tornando impossível o teste de algumas regras.

2. Adicionadas regras para não aceitar saque nem depósitos de valor menores ou iguais a Zero.

3. Ao invés de variáveis globais, foi utilizado uma classe para armazenar as informações do cliente/usuário.

<h1 align=center>Alterações v2</h4>
Arquivo atualizado em 27/03/2025
<h4> Melhorada a estrutura do código e adicionadas duas novas funcionalidades, cadastro de cliente(criar usuário) e cadastro de conta(criar conta corrente).</h4>

# Criar usuário (cliente)
```yaml
1. Os usuários devem ser armazenados em uma LISTA.
2. Dados para cadastrar um usuário: nome, data de nascimento, cpf e endereço.
3. Endereço deve ser uma STRING com o formato: logradouro, número, bairro, cidade/UF.
4. O CPF deve ser amazenado somente os números.
5. Não deve ser possível cadastrar 2 usuários com o mesmo CPF.
```
# Criar Conta Corrente
```yaml
1. As contas devem ser armazenados em uma LISTA.
2. A conta é composta por: Agência, número da conta e usuário.
3. Número da conta deve ser sequencial iniciando em 1.
4. O número da agência deve ser fixo "0001".
5. Um usuário pode ter diversas contas.
6. Cada conta pode pertencer a apenas 1 usuário.
