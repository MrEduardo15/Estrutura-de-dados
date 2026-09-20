# Representacao da entidade Pedido
class Pedido:
    def __init__(self, id_pedido: int, descricao: str, prioridade: int):
        self.id = id_pedido
        self.descricao = descricao
        self.prioridade = prioridade

    def __str__(self):
        return f"ID: {self.id} | Descricao: {self.descricao} | Prioridade: {self.prioridade}"


# Estrutura do Max-Heap armazenado em vetor
class Heap:
    def __init__(self, capacidade_inicial: int = 10):
        self.dados = []
        self.tamanho = 0
        self.capacidade = capacidade_inicial

    # Operacao: inicializar_heap
    def inicializar_heap(self, capacidade_inicial: int = 10, vetor_inicial: list = None):
        if vetor_inicial is not None:
            self.dados = list(vetor_inicial)
            self.tamanho = len(vetor_inicial)
            self.capacidade = max(capacidade_inicial, self.tamanho)
            self.construir()
        else:
            self.dados = []
            self.tamanho = 0
            self.capacidade = capacidade_inicial

    # Operacoes auxiliares de relacionamentos entre indices
    def pai(self, i: int) -> int:
        return (i - 1) // 2

    def esquerdo(self, i: int) -> int:
        return 2 * i + 1

    def direito(self, i: int) -> int:
        return 2 * i + 2

    # Operacao: max_heapfy
    def max_heapfy(self, i: int):
        esq = self.esquerdo(i)
        dir_idx = self.direito(i)
        maior = i

        if esq < self.tamanho and self.dados[esq].prioridade > self.dados[maior].prioridade:
            maior = esq

        if dir_idx < self.tamanho and self.dados[dir_idx].prioridade > self.dados[maior].prioridade:
            maior = dir_idx

        if maior != i:
            self.dados[i], self.dados[maior] = self.dados[maior], self.dados[i]
            self.max_heapfy(maior)

    # Operacao: construir
    def construir(self):
        inicio = (self.tamanho // 2) - 1
        for i in range(inicio, -1, -1):
            self.max_heapfy(i)

    # Operacao: inserir
    def inserir(self, pedido: Pedido):
        if self.tamanho >= self.capacidade:
            self.capacidade *= 2

        self.dados.append(pedido)
        self.tamanho += 1

        atual = self.tamanho - 1
        while atual > 0 and self.dados[atual].prioridade > self.dados[self.pai(atual)].prioridade:
            p_idx = self.pai(atual)
            self.dados[atual], self.dados[p_idx] = self.dados[p_idx], self.dados[atual]
            atual = p_idx

    # Operacao: remover
    def remover(self) -> Pedido:
        if self.tamanho == 0:
            return None

        raiz = self.dados[0]

        if self.tamanho == 1:
            self.dados.pop()
            self.tamanho -= 1
            return raiz

        self.dados[0] = self.dados.pop()
        self.tamanho -= 1
        self.max_heapfy(0)

        return raiz

    # Operacao: print_heap
    def print_heap(self):
        if self.tamanho == 0:
            print("Nenhum pedido cadastrado.")
            return

        print("Pedidos no Heap:")
        for i in range(self.tamanho):
            print(f"ID: {self.dados[i].id} | Prioridade: {self.dados[i].prioridade} | Descricao: {self.dados[i].descricao}")


def exibir_opcoes_menu():
    print("\n==============================================")
    print("SISTEMA DE GERENCIAMENTO DE PEDIDOS (MAX-HEAP)")
    print("==============================================")
    print("Opcoes do Menu Principal:")
    print("  [1] - Cadastrar pedido")
    print("  [2] - Atender pedido de maior prioridade")
    print("  [3] - Exibir lista de pedidos")
    print("  [4] - Exibir quantidade de pedidos aguardando")
    print("  [5] - Construir Heap a partir de lote inicial")
    print("  [0] - Sair")
    print("==============================================")


def menu():
    heap = Heap()
    heap.inicializar_heap()

    while True:
        exibir_opcoes_menu()
        print("Opcoes validas: Digite 1, 2, 3, 4, 5 ou 0")
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            print("\n--- CADASTRO DE NOVO PEDIDO ---")
            
            # Campo ID
            while True:
                print("\nCampo: ID do Pedido")
                print("Opcoes validas: Digite um numero inteiro positivo (ex: 101, 102)")
                id_input = input("Digite o ID: ").strip()
                if id_input.isdigit() and int(id_input) > 0:
                    id_pedido = int(id_input)
                    break
                print("Erro: Entrada invalida. Digite apenas numeros inteiros maiores que zero.")

            # Campo Descricao
            while True:
                print("\nCampo: Descricao do Pedido")
                print("Opcoes validas: Texto descrevendo o pedido (nao pode ser vazio)")
                descricao = input("Digite a Descricao: ").strip()
                if len(descricao) > 0:
                    break
                print("Erro: A descricao nao pode ser vazia.")

            # Campo Prioridade
            while True:
                print("\nCampo: Prioridade do Pedido")
                print("Opcoes validas: Digite um numero inteiro (quanto maior o valor, maior a prioridade)")
                print("Exemplo: 1 (baixa), 5 (media), 10 (urgente)")
                prio_input = input("Digite a Prioridade: ").strip()
                if prio_input.isdigit():
                    prioridade = int(prio_input)
                    break
                print("Erro: Entrada invalida. Digite apenas numeros inteiros positivos.")

            pedido = Pedido(id_pedido, descricao, prioridade)
            heap.inserir(pedido)
            print("\nPedido cadastrado e inserido no Heap com sucesso!")

        elif opcao == "2":
            print("\n--- ATENDIMENTO DE PEDIDO ---")
            print("Opcoes validas: [S] Confirmar atendimento | [N] Cancelar")
            confirmar = input("Deseja atender o pedido de maior prioridade agora? (S/N): ").strip().upper()
            
            if confirmar == "S":
                pedido_atendido = heap.remover()
                if pedido_atendido:
                    print("\nPedido Atendido com Sucesso:")
                    print(f"  ID: {pedido_atendido.id}")
                    print(f"  Descricao: {pedido_atendido.descricao}")
                    print(f"  Prioridade: {pedido_atendido.prioridade}")
                else:
                    print("\nNao ha pedidos aguardando atendimento.")
            else:
                print("Atendimento cancelado.")

        elif opcao == "3":
            print("\n--- LISTA DE PEDIDOS AGUARDANDO ---")
            heap.print_heap()

        elif opcao == "4":
            print("\n--- QUANTIDADE DE PEDIDOS ---")
            print(f"Total de pedidos aguardando atendimento: {heap.tamanho}")

        elif opcao == "5":
            print("\n--- CARREGAR LOTE INICIAL DE TESTES ---")
            print("Opcoes validas: [S] Carregar lote de 5 pedidos | [N] Cancelar")
            confirmar = input("Isso ira redefinir o Heap atual. Deseja continuar? (S/N): ").strip().upper()

            if confirmar == "S":
                lote = [
                    Pedido(1, "Pedido A", 2),
                    Pedido(2, "Pedido B", 5),
                    Pedido(3, "Pedido C", 3),
                    Pedido(4, "Pedido D", 8),
                    Pedido(5, "Pedido E", 1)
                ]
                heap.inicializar_heap(vetor_inicial=lote)
                print("Lote inicial carregado e Max-Heap construido com sucesso!")
            else:
                print("Operacao cancelada.")

        elif opcao == "0":
            print("\nEncerrando a aplicacao...")
            break
        else:
            print("\nOpcao invalida. Por favor, escolha uma das opcoes listadas no menu.")
            

if __name__ == "__main__":
    menu()