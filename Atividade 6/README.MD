# Tabela Hash com Encadeamento Externo

Trabalho pratico da disciplina de Estrutura de Dados focado no estudo e aplicacao do tratamento de colisoes em Tabela Hash utilizando encadeamento externo (listas encadeadas).

## Especificacoes Tecnicas

- Funcao Hash: h(k) = k mod 7
- Tamanho da Tabela: 7
- Tratamento de Colisoes: Encadeamento Externo
- Conjunto de Entrada: {190, 322, 172, 89, 13, 4, 769, 61, 15, 76}

## Resultados Principais

- Total de elementos inseridos: 10
- Fator de Carga final: 1.43
- Distribuicao das chaves por indice:
  - Indice 0: 322
  - Indice 1: 190, 15
  - Indice 2: Vazio
  - Indice 3: Vazio
  - Indice 4: 172, 4
  - Indice 5: 89, 61
  - Indice 6: 13, 769, 76

## Instrucoes de Execucao

### Executando em Python
python tabela_hash.py

### Executando em C
gcc tabela_hash.c -o tabela_hash
./tabela_hash