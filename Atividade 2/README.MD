# Gerenciador de Playlist com Lista Encadeada

Trabalho prático de Estrutura de Dados focado no desenvolvimento de uma aplicação para gerenciamento de playlists de música utilizando uma Lista Simplesmente Encadeada implementada manualmente em Python.

## Estrutura do Código

O código-fonte está organizado nas seguintes classes no arquivo playlist.py:

- Musica: Armazena os dados da música (id, titulo, artista, album, duracao).
- No: Representa o nó da lista contendo o objeto musica e a referência para o proximo nó.
- ListaEncadeada: Classe principal com a estrutura da lista, mantendo as referências primeiro e quantidade.

## Operações Implementadas

A classe ListaEncadeada implementa os seguintes métodos:

- inicializar_lista: Define o ponteiro inicial como nulo e zera a contagem de nós.
- inserir: Suporta inserção no início, em posição específica (meio) ou no final da lista.
- imprimir: Percorre a lista exibindo todas as músicas armazenadas.
- buscar: Permite realizar buscas por ID único ou por nome de artista.
- remover: Altera as referências entre os nós para remover uma música pelo ID.
- duracao_total: Calcula o tempo total acumulado da playlist em segundos.

---

## Instruções para Execução

### Pré-requisitos
- Python 3 instalado no sistema.

### Passo a Passo
Clone o repositório e execute o script pelo terminal para rodar o programa e a suíte de testes:

python playlist.py

---

## Conjunto de Testes Realizados

A função executar_testes() valida os seguintes cenários de teste obrigatórios:

1. Criação de uma playlist vazia
2. Inserção da primeira música
3. Inserção no final
4. Inserção no início
5. Inserção no meio
6. Inserção de várias músicas
7. Busca de música existente
8. Busca de música inexistente
9. Busca por artista
10. Cálculo da quantidade de músicas
11. Cálculo da duração total
12. Remoção da primeira música
13. Remoção de música intermediária
14. Remoção da última música
15. Tentativa de remoção de música inexistente
16. Remoção da única música da playlist

---

## Exemplo de Saída no Terminal

Executando testes da playlist...

--- PLAYLIST (Quantidade: 5) ---
Posicao 0: [3] Imagine - John Lennon (Imagine) - 03:03
Posicao 1: [4] Another One Bites the Dust - Queen (The Game) - 03:35
Posicao 2: [1] Bohemian Rhapsody - Queen (A Night at the Opera) - 05:54
Posicao 3: [2] Hotel California - Eagles (Hotel California) - 06:31
Posicao 4: [5] Smells Like Teen Spirit - Nirvana (Nevermind) - 05:01
------------------------------------------

Todos os testes obrigatorios executados com sucesso!