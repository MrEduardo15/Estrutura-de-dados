# Representacao do elemento Musica
class Musica:
    def __init__(self, id_musica: int, titulo: str, artista: str, album: str, duracao: int):
        self.id = id_musica
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracao = duracao

    def __str__(self):
        minutos = self.duracao // 60
        segundos = self.duracao % 60
        return f"[{self.id}] {self.titulo} - {self.artista} ({self.album}) - {minutos:02d}:{segundos:02d}"


# Representacao do No da lista
class No:
    def __init__(self, musica: Musica):
        self.musica = musica
        self.proximo = None


# Estrutura da Lista Encadeada
class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.quantidade = 0

    # Operacao: inicializar_lista
    def inicializar_lista(self):
        self.primeiro = None
        self.quantidade = 0

    # Operacao: inserir (inicio, meio ou final)
    def inserir(self, musica: Musica, posicao: int = None):
        novo_no = No(musica)

        # Inserir no inicio
        if self.primeiro is None or posicao == 0:
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no
            self.quantidade += 1
            return

        # Inserir no final
        if posicao is None or posicao >= self.quantidade:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
            self.quantidade += 1
            return

        # Inserir em posicao determinada
        atual = self.primeiro
        i = 0
        while atual is not None and i < posicao - 1:
            atual = atual.proximo
            i += 1

        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
        self.quantidade += 1

    # Operacao: imprimir
    def imprimir(self):
        if self.primeiro is None:
            print("Playlist vazia.")
            return

        atual = self.primeiro
        pos = 0
        print(f"\n--- PLAYLIST (Quantidade: {self.quantidade}) ---")
        while atual is not None:
            print(f"Posicao {pos}: {atual.musica}")
            atual = atual.proximo
            pos += 1
        print("------------------------------------------\n")

    # Operacao: buscar (por ID ou por Artista)
    def buscar(self, id_musica: int = None, artista: str = None):
        if self.primeiro is None:
            return None if id_musica is not None else []

        # Buscar por ID
        if id_musica is not None:
            atual = self.primeiro
            while atual is not None:
                if atual.musica.id == id_musica:
                    return atual.musica
                atual = atual.proximo
            return None

        # Buscar por Artista
        if artista is not None:
            resultados = []
            atual = self.primeiro
            while atual is not None:
                if artista.lower() in atual.musica.artista.lower():
                    resultados.append(atual.musica)
                atual = atual.proximo
            return resultados

        return None

    # Operacao: remover
    def remover(self, id_musica: int) -> bool:
        if self.primeiro is None:
            return False

        # Remover primeira musica
        if self.primeiro.musica.id == id_musica:
            self.primeiro = self.primeiro.proximo
            self.quantidade -= 1
            return True

        # Remover musica intermediaria ou ultima
        atual = self.primeiro
        while atual.proximo is not None:
            if atual.proximo.musica.id == id_musica:
                atual.proximo = atual.proximo.proximo
                self.quantidade -= 1
                return True
            atual = atual.proximo

        return False

    # Calculo da duracao total
    def duracao_total(self) -> int:
        total = 0
        atual = self.primeiro
        while atual is not None:
            total += atual.musica.duracao
            atual = atual.proximo
        return total


# Casos de teste obrigatorios
def executar_testes():
    print("Executando testes da playlist...")

    # Teste: Criacao de uma playlist vazia
    p = ListaEncadeada()
    p.inicializar_lista()
    assert p.quantidade == 0 and p.primeiro is None

    # Teste: Insercao da primeira musica
    m1 = Musica(1, "Bohemian Rhapsody", "Queen", "A Night at the Opera", 354)
    p.inserir(m1)
    assert p.quantidade == 1 and p.primeiro.musica.id == 1

    # Teste: Insercao no final
    m2 = Musica(2, "Hotel California", "Eagles", "Hotel California", 391)
    p.inserir(m2)
    assert p.quantidade == 2

    # Teste: Insercao no inicio
    m3 = Musica(3, "Imagine", "John Lennon", "Imagine", 183)
    p.inserir(m3, posicao=0)
    assert p.primeiro.musica.id == 3

    # Teste: Insercao no meio
    m4 = Musica(4, "Another One Bites the Dust", "Queen", "The Game", 215)
    p.inserir(m4, posicao=1)
    assert p.quantidade == 4

    # Teste: Insercao de varias musicas
    m5 = Musica(5, "Smells Like Teen Spirit", "Nirvana", "Nevermind", 301)
    p.inserir(m5)
    assert p.quantidade == 5

    # Exibe a playlist
    p.imprimir()

    # Teste: Busca de musica existente
    assert p.buscar(id_musica=1).titulo == "Bohemian Rhapsody"

    # Teste: Busca de musica inexistente
    assert p.buscar(id_musica=99) is None

    # Teste: Busca por artista
    assert len(p.buscar(artista="Queen")) == 2

    # Teste: Calculo da quantidade de musicas
    assert p.quantidade == 5

    # Teste: Calculo da duracao total
    assert p.duracao_total() == 1444

    # Teste: Remocao da primeira musica
    assert p.remover(3) is True
    assert p.primeiro.musica.id == 4

    # Teste: Remocao de musica intermediaria
    assert p.remover(1) is True

    # Teste: Remocao da ultima musica
    assert p.remover(5) is True

    # Teste: Tentativa de remocao de musica inexistente
    assert p.remover(999) is False

    # Teste: Remocao da unica musica da playlist
    p.remover(4)
    assert p.remover(2) is True
    assert p.quantidade == 0 and p.primeiro is None

    print("Todos os testes obrigatorios executados com sucesso!")


if __name__ == "__main__":
    executar_testes()