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

#informe o tamanho; 
def vetorsize():
    n = int(input("Digite o tamanho do vetor: "))
    vetor = []
    for i in range(n):
        elemento = int(input(f"Digite o elemento {i+1}: "))
        vetor.append(elemento)
    print(vetor)

vetorsize()