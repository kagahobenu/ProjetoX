lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# Maior elemento
maior = 0

for i in range(0, len(lista)):
    if (maior < lista[i]):
        maior = lista[i]
print(maior)
# Menor elemento

menor = lista[0]

for i in range(0, len(lista)):
    if (menor > lista[i]):
        menor = lista[i]
print(menor)

# Números pares

listaPares = []
for i in range(0, len(lista)):
    if (lista[i] % 2 == 0 and lista[i] > 0):
        listaPares.append(lista[i])
print(listaPares)

# Ocorrências

ocorrencias = 0
for i in range(0, len(lista)):
    if (lista[i] == lista[0]):
        ocorrencias += 1
print(ocorrencias)

# Média dos elementos

media = 0
soma = 0
for i in range(0, len(lista)):
    soma += lista[i]
media = soma / len(lista)
print(f'{media:.2f}')

# Soma dos elementos de valor negativo

somaNegativo = 0

for i in range(0, len(lista)):
    if(lista[i] < 0):
        somaNegativo += lista[i]
print(somaNegativo)
