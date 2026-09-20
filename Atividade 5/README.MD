# Sistema de Gerenciamento de Pedidos com Max-Heap

Trabalho pratico da disciplina de Estrutura de Dados focado no desenvolvimento de um sistema de gerenciamento de pedidos com fila de prioridades utilizando a estrutura de dados Max-Heap implementada em vetor dinamico em Python.

## Estrutura do Codigo

O codigo-fonte esta dividido nas seguintes classes no arquivo sistema_pedidos.py:

- Pedido: Armazena os dados do pedido (id, descricao, prioridade).
- Heap: Implementa a estrutura do Max-Heap em vetor, contendo os atributos dados, tamanho e capacidade, alem das relacoes de indices para arvore completa.

## Operacoes do Heap Implementadas

- inicializar_heap: Cria uma estrutura limpa ou constroi o heap a partir de um vetor inicial.
- inserir: Adiciona um novo pedido ao final do vetor e reorganiza subindo pela arvore.
- remover: Retorna e remove o pedido de maior prioridade (raiz), reorganizando a arvore de cima para baixo.
- max_heapfy: Garante a propriedade do Max-Heap ajustando os nos pai e filhos.
- construir: Transforma um vetor desordenado em um Max-Heap valido.
- print_heap: Exibe os pedidos armazenados sequencialmente no vetor.

---

## Relacao de Indices do Vetor

A representacao da arvore binaria sobre o vetor utiliza as seguintes formulas para um elemento no indice i:

- pai = (i - 1) / 2
- esquerdo = 2 * i + 1
- direito = 2 * i + 2

---

## Instrucoes para Execucao

### Pre-requisitos
- Python 3 instalado no sistema.

### Executando o Sistema
Para rodar a aplicacao via terminal, execute o comando:

python sistema_pedidos.py

---

## Exemplo de Execucao no Terminal

==============================================
SISTEMA DE GERENCIAMENTO DE PEDIDOS (MAX-HEAP)
==============================================
Opcoes do Menu Principal:
  [1] - Cadastrar pedido
  [2] - Atender pedido de maior prioridade
  [3] - Exibir lista de pedidos
  [4] - Exibir quantidade de pedidos aguardando
  [5] - Construir Heap a partir de lote inicial
  [0] - Sair
==============================================
Opcoes validas: Digite 1, 2, 3, 4, 5 ou 0
Escolha uma opcao: 1

--- CADASTRO DE NOVO PEDIDO ---

Campo: ID do Pedido
Opcoes validas: Digite um numero inteiro positivo (ex: 101, 102)
Digite o ID: 101

Campo: Descricao do Pedido
Opcoes validas: Texto descrevendo o pedido (nao pode ser vazio)
Digite a Descricao: Pedido urgente de suprimentos

Campo: Prioridade do Pedido
Opcoes validas: Digite um numero inteiro (quanto maior o valor, maior a prioridade)
Exemplo: 1 (baixa), 5 (media), 10 (urgente)
Digite a Prioridade: 10

Pedido cadastrado e inserido no Heap com sucesso!

==============================================
SISTEMA DE GERENCIAMENTO DE PEDIDOS (MAX-HEAP)
==============================================
Opcoes do Menu Principal:
  [1] - Cadastrar pedido
  [2] - Atender pedido de maior prioridade
  [3] - Exibir lista de pedidos
  [4] - Exibir quantidade de pedidos aguardando
  [5] - Construir Heap a partir de lote inicial
  [0] - Sair
==============================================
Opcoes validas: Digite 1, 2, 3, 4, 5 ou 0
Escolha uma opcao: 2

--- ATENDIMENTO DE PEDIDO ---
Opcoes validas: [S] Confirmar atendimento | [N] Cancelar
Deseja atender o pedido de maior prioridade agora? (S/N): S

Pedido Atendido com Sucesso:
  ID: 101
  Descricao: Pedido urgente de suprimentos
  Prioridade: 10