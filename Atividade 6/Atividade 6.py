# Representacao do No da lista encadeada
class No:
    def __init__(self, chave: int):
        self.chave = chave
        self.proximo = None


# Estrutura da Tabela Hash com Encadeamento Externo
class TabelaHash:
    def __init__(self, tamanho: int = 7):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.total_elementos = 0

    # Funcao Hash
    def _hash(self, chave: int) -> int:
        return chave % self.tamanho

    # Operacao: Inserir
    def inserir(self, chave: int):
        indice = self._hash(chave)
        novo_no = No(chave)

        if self.tabela[indice] is None:
            self.tabela[indice] = novo_no
        else:
            atual = self.tabela[indice]
            while atual.proximo is not None:
                if atual.chave == chave:
                    return  # Evita duplicatas
                atual = atual.proximo
            if atual.chave == chave:
                return
            atual.proximo = novo_no

        self.total_elementos += 1

    # Operacao: Remover
    def remover(self, chave: int) -> bool:
        indice = self._hash(chave)
        atual = self.tabela[indice]
        anterior = None

        while atual is not None:
            if atual.chave == chave:
                if anterior is None:
                    self.tabela[indice] = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.total_elementos -= 1
                return True
            anterior = atual
            atual = atual.proximo

        return False

    # Operacao: Imprimir Tabela
    def imprimir(self):
        print("\n--- ESTADO DA TABELA HASH ---")
        for i in range(self.tamanho):
            print(f"Indice {i}: ", end="")
            atual = self.tabela[i]
            if atual is None:
                print("NULL")
            else:
                elementos = []
                while atual is not None:
                    elementos.append(str(atual.chave))
                    atual = atual.proximo
                print(" -> ".join(elementos) + " -> NULL")
        print("-----------------------------\n")

    # Operacao: Fator de Carga
    def fator_de_carga(self) -> float:
        return self.total_elementos / self.tamanho


def executar():
    chaves = [190, 322, 172, 89, 13, 4, 769, 61, 15, 76]
    ht = TabelaHash(tamanho=7)

    # Insercao dos elementos
    for c in chaves:
        ht.inserir(c)

    # Exibe a tabela montada
    ht.imprimir()
    print(f"Fator de Carga: {ht.fator_de_carga():.2f}")

    # Teste de remocao
    print("\nRemovendo a chave 172...")
    ht.remover(172)
    print("Removendo a chave 769...")
    ht.remover(769)

    ht.imprimir()


if __name__ == "__main__":
    executar()