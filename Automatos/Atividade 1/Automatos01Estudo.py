class Automato:
    def __init__(self, regras, inicial, finais):
        self.regras = regras
        self.inicial = inicial
        self.finais = set(finais)

    def testar(self, texto):
        atual = self.inicial
        caminho = [atual]

        for char in str(texto):
            # Se a transição não existir, quebra o loop direto
            if (atual, char) not in self.regras:
                return False, caminho
            
            atual = self.regras[(atual, char)]
            caminho.append(atual)

        return atual in self.finais, caminho


# Configuração do AFD
regras_transicao = {
    ('q1', '0'): 'q1', ('q1', '1'): 'q2',
    ('q2', '1'): 'q2', ('q2', '0'): 'q3',
    ('q3', '0'): 'q2', ('q3', '1'): 'q2'
}

dfa = Automato(regras_transicao, 'q1', ['q2'])

# Testes rápidos
testes = ["1", "001", "10", "100", "1101", "00", "1000"]

for t in testes:
    ok, passos = dfa.testar(t)
    print(f"{t} -> {'OK' if ok else 'X'} | Rota: {passos}")
