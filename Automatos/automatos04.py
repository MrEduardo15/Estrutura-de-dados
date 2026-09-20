import sys

def fecho_epsilon_estado(estado, trans_vazio):
    """Retorna a lista de estados alcançáveis a partir de 'estado' via transições 'vazio'."""
    visitados = [estado]
    fila = [estado]
    while fila:
        atual = fila.pop(0)
        para_onde = trans_vazio.get(atual, [])
        for prox in para_onde:
            if prox not in visitados and prox != 'vazio':
                visitados.append(prox)
                fila.append(prox)
    return visitados

def expandir_estados(lista_estados, trans_vazio):
    """Aplica o fecho-épsilon para cada estado mantendo a ordem e multiplicidade."""
    resultado = []
    for est in lista_estados:
        resultado.extend(fecho_epsilon_estado(est, trans_vazio))
    return resultado

def simular_afn():
    conteudo = sys.stdin.read().splitlines()
    linhas = [l.strip() for l in conteudo if l.strip()]
    
    if not linhas:
        return

    # 1. Leitura do Autômato
    estados = linhas[0].split()
    alfabeto = linhas[1].split()
    estado_inicial = linhas[2].strip()
    estados_finais = set(linhas[3].split())

    transicoes = {}
    trans_vazio = {}

    qtd_simbolos = len(alfabeto)
    idx_linha = 4

    for _ in range(len(estados)):
        partes = linhas[idx_linha].split()
        estado_atual = partes[0]

        # Transições para cada símbolo do alfabeto
        for i, simbolo in enumerate(alfabeto):
            destino = partes[1 + i]
            if destino != 'vazio':
                transicoes[(estado_atual, simbolo)] = destino.split(',')
            else:
                transicoes[(estado_atual, simbolo)] = []

        # Transição por 'vazio' (épsilon)
        destino_vazio = partes[1 + qtd_simbolos]
        if destino_vazio != 'vazio':
            trans_vazio[estado_atual] = destino_vazio.split(',')
        else:
            trans_vazio[estado_atual] = []

        idx_linha += 1

    # 2. Leitura da palavra
    palavra = linhas[idx_linha].strip() if idx_linha < len(linhas) else ""
    if palavra == "vazio":
        palavra = ""

    # 3. Processamento
    estados_atuais = expandir_estados([estado_inicial], trans_vazio)
    print(estados_atuais)

    for simbolo in palavra:
        print(simbolo)
        proximos = []
        for est in estados_atuais:
            dests = transicoes.get((est, simbolo), [])
            proximos.extend(dests)
        estados_atuais = expandir_estados(proximos, trans_vazio)
        print(estados_atuais)

    # 4. Decisão de Aceitação
    se_aceita = any(est in estados_finais for est in estados_atuais)
    if se_aceita:
        print("aceita")
    else:
        print("rejeita")

if __name__ == "__main__":
    simular_afn()