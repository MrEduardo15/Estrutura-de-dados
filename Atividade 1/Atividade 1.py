#O programa deverá permitir que o usuário:
#informe o tamanho;
#crie dois ou mais vetores;
#informe os valores reais de cada vetor;
#exiba os vetores armazenados;
#multiplique um vetor por um valor escalar;
#calcule a soma de dois vetores;
#calcule o produto escalar entre dois vetores;
#calcule a norma de um vetor;
#calcule a similaridade de cosseno entre dois vetores;
#determine, entre um conjunto de vetores, qual possui maior similaridade com um vetor de consulta.

import math


# ==========================================
# OPERAÇÕES BÁSICAS DO ARRAY
# ==========================================


def inicializar_array(tamanho):
    # Permite que o usuário informe o tamanho;
    array = [0.0] * tamanho
    return array


def inserir(vetor, posicao, valor):
    # Permite que o usuário informe os valores reais de cada vetor;
    vetor[posicao] = float(valor)


def imprimir(vetor):
    # Permite que o usuário exiba os vetores armazenados;
    print("[", end="")
    for i in range(len(vetor)):
        print(f"{vetor[i]:.4f}", end="")
        if i < len(vetor) - 1:
            print(", ", end="")
    print("]")


def buscar(vetor, elemento):
    for i in range(len(vetor)):
        if vetor[i] == elemento:
            return i
    return -1


def remover(vetor, posicao):
    vetor[posicao] = 0.0

# OPERAÇÕES MATEMÁTICAS

def multiplicar_por_escalar(vetor, k):
    # Permite que o usuário multiplique um vetor por um valor escalar;
    resultado = inicializar_array(len(vetor))
    for i in range(len(vetor)):
        resultado[i] = vetor[i] * k
    return resultado


def somar_vetores(vetor1, vetor2):
    # Permite que o usuário calcule a soma de dois vetores;
    if len(vetor1) != len(vetor2):
        print("Erro: Os vetores precisam ter o mesmo tamanho!")
        return None

    resultado = inicializar_array(len(vetor1))
    for i in range(len(vetor1)):
        resultado[i] = vetor1[i] + vetor2[i]
    return resultado


def produto_escalar(vetor1, vetor2):
    # Permite que o usuário calcule o produto escalar entre dois vetores;
    if len(vetor1) != len(vetor2):
        print("Erro: Os vetores precisam ter o mesmo tamanho!")
        return None

    soma = 0.0
    for i in range(len(vetor1)):
        soma = soma + (vetor1[i] * vetor2[i])
    return soma


def norma_vetor(vetor):
    # Permite que o usuário calcule a norma de um vetor;
    soma_quadrados = 0.0
    for i in range(len(vetor)):
        soma_quadrados = soma_quadrados + (vetor[i] ** 2)
    return math.sqrt(soma_quadrados)


def similaridade_cosseno(vetor1, vetor2):
    # Permite que o usuário calcule a similaridade de cosseno entre dois vetores;
    norma1 = norma_vetor(vetor1)
    norma2 = norma_vetor(vetor2)

    if norma1 == 0 or norma2 == 0:
        print("Operacao invalida: vetor nulo.")
        return None

    prod = produto_escalar(vetor1, vetor2)
    return prod / (norma1 * norma2)


def maior_similaridade(vetor_consulta, lista_vetores):
    # Permite que o usuário determine, entre um conjunto de vetores, qual possui maior similaridade com um vetor de consulta.
    melhor_posicao = -1
    maior_similaridade = -1.0

    for i in range(len(lista_vetores)):
        sim = similaridade_cosseno(vetor_consulta, lista_vetores[i])
        if sim != None and sim > maior_similaridade:
            maior_similaridade = sim
            melhor_posicao = i

    return melhor_posicao


# ==========================================
# PROGRAMA PRINCIPAL / TESTES
# ==========================================

# Permite que o usuário crie dois ou mais vetores;
v1 = inicializar_array(4)
v2 = inicializar_array(4)

# Inserindo dados do exemplo do enunciado
dados_v1 = [0.8, 0.2, 0.5, 0.9]
dados_v2 = [0.7, 0.1, 0.6, 0.8]

for i in range(4):
    inserir(v1, i, dados_v1[i])
    inserir(v2, i, dados_v2[i])

print("Vetor A: ", end="")
imprimir(v1)

print("Vetor B: ", end="")
imprimir(v2)

# Multiplicação por escalar
v_mult = multiplicar_por_escalar(v1, 2.0)
print("\nVetor A multiplicado por 2: ", end="")
imprimir(v_mult)

# Soma
v_soma = somar_vetores(v1, v2)
print("Soma A + B: ", end="")
imprimir(v_soma)

# Produto Escalar
prod = produto_escalar(v1, v2)
print(f"Produto escalar: {prod:.4f}")

# Norma
norma = norma_vetor(v1)
print(f"Norma do Vetor A: {norma:.4f}")

# Similaridade de Cosseno
sim = similaridade_cosseno(v1, v2)
print(f"Similaridade de Cosseno: {sim:.4f}")

# Teste com conjunto de vetores
print("\nBuscando maior similaridade no conjunto:")
v3 = inicializar_array(4)
inserir(v3, 0, 0.1)
inserir(v3, 1, 0.1)
inserir(v3, 2, 0.1)
inserir(v3, 3, 0.1)

conjunto = [v1, v2, v3]
posicao = maior_similaridade(v1, conjunto)
print(f"O vetor com maior similaridade com Vetor A esta na posicao: {posicao}")