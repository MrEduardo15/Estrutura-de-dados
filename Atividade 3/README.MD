# Torre de Hanoi com Pilhas Dinamicas

Trabalho pratico da disciplina de Estrutura de Dados focado na implementacao do jogo Torre de Hanoi utilizando Pilhas Encadeadas Dinamicas em Python.

## Estrutura do Codigo

O codigo-fonte esta organizado nas seguintes estruturas no arquivo hanoi.py:

- No: Representa o no da pilha, contendo o valor do disco e a referencia proximo.
- Pilha: Classe que implementa a estrutura de pilha encadeada e suas operacoes basicas.
- TorreDeHanoi: Controla as tres pilhas (torres), valida as regras dos movimentos e contabiliza as jogadas.

## Operacoes da Pilha Implementadas

- inicializar_pilha: Limpa a pilha e zera a contagem de elementos.
- empilhar: Adiciona um novo disco no topo da pilha.
- desempilhar: Remove e retorna o disco do topo da pilha.
- topo: Retorna o valor do disco do topo sem remove-lo.
- imprimir: Exibe os elementos armazenados na pilha.

---

## Instrucoes para Execucao

### Pre-requisitos
- Python 3 instalado no sistema.

### Executando o Jogo
Para iniciar o jogo interativo no terminal, execute o comando:

python hanoi.py

---

## Regras e Validacoes

O jogo contem 4 discos inicialmente empilhados na Torre 1 e aplica as seguintes regras:

1. Apenas o disco do topo pode ser movimentado.
2. Nao e possivel mover discos de uma torre vazia.
3. Nao e permitido colocar um disco maior sobre um disco menor.
4. O objetivo e mover todos os 4 discos para a Torre 3.

---

## Exemplo de Execucao no Terminal

Movimentos realizados: 0
Torre 1: [4, 3, 2, 1]
Torre 2: []
Torre 3: []

Opcoes:
1 - Realizar movimento
2 - Reiniciar partida
0 - Encerrar jogo
Escolha uma opcao: 1
Torre de origem (1-3): 1
Torre de destino (1-3): 2

Movimentos realizados: 1
Torre 1: [4, 3, 2]
Torre 2: [1]
Torre 3: []