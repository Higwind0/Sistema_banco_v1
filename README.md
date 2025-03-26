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
<h1 align=center>Alterações</h4>
<h4>As seguintes alterações foram realizadas por falta de especificação do sistema para melhorar a usabilidade:</h4>


1. Criado um método de retorno para navegação entre os itens. Necessário, pois, caso não houver, o código vai encerrar após cada ação realizada. Dessa forma se tornando impossível o teste de algumas regras.

2. Adicionadas regras para não aceitar saque nem depósitos de valor menores ou iguais a Zero.

3. Ao invés de variáveis globais, foi utilizado uma classe para armazenar as informações do cliente/usuário.


