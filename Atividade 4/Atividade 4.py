import random
import time


# Representacao do No da fila
class No:
    def __init__(self, cor: str):
        self.cor = cor
        self.proximo = None


# Estrutura da Fila Dinamica
class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    # Operacao: inicializar_fila
    def inicializar_fila(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    # Operacao: enfileirar
    def enfileirar(self, cor: str):
        novo_no = No(cor)
        if self.fim is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
        self.quantidade += 1

    # Operacao: desenfileirar
    def desenfileirar(self) -> str:
        if self.inicio is None:
            return None

        cor_removida = self.inicio.cor
        self.inicio = self.inicio.proximo
        self.quantidade -= 1

        if self.inicio is None:
            self.fim = None

        return cor_removida

    # Operacao: frente
    def frente(self) -> str:
        if self.inicio is None:
            return None
        return self.inicio.cor

    # Operacao: imprimir
    def imprimir(self):
        elementos = []
        atual = self.inicio
        while atual is not None:
            elementos.append(atual.cor)
            atual = atual.proximo
        print(" -> ".join(elementos))


# Estrutura do Jogo Genius
class JogoGenius:
    CORES_DISPONIVEIS = ["VERDE", "VERMELHO", "AMARELO", "AZUL"]

    def __init__(self):
        self.sequencia_jogo = Fila()
        self.pontuacao = 0

    def iniciar_partida(self):
        self.sequencia_jogo.inicializar_fila()
        self.pontuacao = 0
        self.adicionar_cor()

    def adicionar_cor(self):
        cor_sorteada = random.choice(self.CORES_DISPONIVEIS)
        self.sequencia_jogo.enfileirar(cor_sorteada)

    def exibir_sequencia(self):
        print("\nAtencao! Memorize a sequencia:")
        atual = self.sequencia_jogo.inicio
        while atual is not None:
            print(f"[{atual.cor}]", end=" ", flush=True)
            time.sleep(1)
            atual = atual.proximo
        print("\n" + "=" * 30)

    def processar_rodada(self) -> bool:
        self.exibir_sequencia()

        # Fila auxiliar para validar as respostas mantendo a ordem original
        fila_auxiliar = Fila()
        fila_auxiliar.inicializar_fila()

        acertou = True
        tamanho_rodada = self.sequencia_jogo.quantidade

        print(f"Sua vez! Digite a sequencia de {tamanho_rodada} cor(es).")
        print(f"Cores validas: {', '.join(self.CORES_DISPONIVEIS)}\n")

        for i in range(1, tamanho_rodada + 1):
            cor_esperada = self.sequencia_jogo.desenfileirar()
            fila_auxiliar.enfileirar(cor_esperada)

            if acertou:
                resposta = input(f"Cor {i}: ").strip().upper()

                if resposta != cor_esperada:
                    print(f"\nResposta incorreta! A cor esperada era {cor_esperada}.")
                    acertou = False

        # Restaura a fila original com os elementos salvos na auxiliar
        while fila_auxiliar.inicio is not None:
            self.sequencia_jogo.enfileirar(fila_auxiliar.desenfileirar())

        if acertou:
            self.pontuacao += 1
            print(f"\nExcelente! Voce acertou a rodada. Pontuacao atual: {self.pontuacao}")
            self.adicionar_cor()
            return True

        return False


def menu():
    jogo = JogoGenius()

    while True:
        print("\n--- JOGO GENIUS ---")
        print("1 - Iniciar nova partida")
        print("0 - Encerrar jogo")
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            jogo.iniciar_partida()
            jogando = True

            while jogando:
                print(f"\n--- RODADA {jogo.pontuacao + 1} ---")
                jogando = jogo.processar_rodada()

            print("\n==================================")
            print("         FIM DE JOGO!             ")
            print(f" Pontuacao final: {jogo.pontuacao} ponto(s)")
            print("==================================")

        elif opcao == "0":
            print("Jogo encerrado.")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    menu()