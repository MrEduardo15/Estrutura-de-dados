# Jogo Genius com Fila Dinamica

Trabalho pratico da disciplina de Estrutura de Dados focado na implementacao do jogo Genius utilizando uma Fila Encadeada Dinamica em Python.

## Estrutura do Codigo

O codigo-fonte esta organizado nas seguintes estruturas no arquivo genius.py:

- No: Representa o no da fila, contendo a string cor e a referencia proximo.
- Fila: Classe que implementa a estrutura de fila encadeada com as referencias inicio e fim.
- JogoGenius: Controla a logica das rodadas, adicao de novas cores, exibicao da sequencia e validacao das respostas do jogador.

## Operacoes da Fila Implementadas

- inicializar_fila: Reseta os ponteiros inicio e fim e zera a contagem de elementos.
- enfileirar: Adiciona uma nova cor ao final da fila.
- desenfileirar: Remove e retorna a cor do inicio da fila.
- frente: Retorna a cor do inicio da fila sem remove-la.
- imprimir: Exibe os elementos armazenados na fila em ordem FIFO.

---

## Instrucoes para Execucao

### Pre-requisitos
- Python 3 instalado no sistema.

### Executando o Jogo
Para iniciar a aplicacao no terminal, execute o comando:

python genius.py

---

## Regras e Funcionamento

1. O jogo sorteia uma cor inicial (VERDE, VERMELHO, AMARELO ou AZUL) e enfileira na sequencia.
2. A sequencia e exibida ao jogador elemento por elemento.
3. O jogador deve informar as cores na mesma ordem apresentada (primeiro que entra e o primeiro que sai).
4. Em caso de acerto, o jogador ganha 1 ponto, uma nova cor e adicionada ao fim da fila e a proxima rodada e iniciada.
5. Se o jogador errar alguma cor, a partida e encerrada e a pontuacao final e exibida.

---

## Exemplo de Execucao no Terminal

--- JOGO GENIUS ---
1 - Iniciar nova partida
0 - Encerrar jogo
Escolha uma opcao: 1

--- RODADA 1 ---

Atencao! Memorize a sequencia:
[AZUL] 
==============================
Sua vez! Digite a sequencia de 1 cor(es).
Cores validas: VERDE, VERMELHO, AMARELO, AZUL

Cor 1: AZUL

Excelente! Voce acertou a rodada. Pontuacao atual: 1

--- RODADA 2 ---

Atencao! Memorize a sequencia:
[AZUL] [VERDE] 
==============================
Sua vez! Digite a sequencia de 2 cor(es).
Cores validas: VERDE, VERMELHO, AMARELO, AZUL

Cor 1: AZUL
Cor 2: VERDE

Excelente! Voce acertou a rodada. Pontuacao atual: 2