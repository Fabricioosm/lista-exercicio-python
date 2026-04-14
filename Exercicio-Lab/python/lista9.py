#Questão 1

'''lista = [1, 5, 10, 6, 9, 3 ]
maior = lista[0]
indice = 0
tam = len(lista)

while indice < tam:
    if lista[indice] > maior:
        maior = lista[indice]
    indice += 1
print(maior)'''

# Questão 2

'''from ProxPrimo import primo

lista = [2, 5, 7, 9, 4, 6, 8, 11] 
acu_primo = 0
i = 0
tam = len(lista)

while i < tam:
    if primo(lista[i]):
        acu_primo += 1
    i += 1
print(acu_primo)'''

# Questão 3

'''lista = ['fabricio', 20, 7, 'medeiros', 5.5]
ind = len(lista) -1

while ind >= 0:
    inversa = lista[ind]
    print(inversa)
    ind -= 1'''

# Questão 4

'''def soma_Lista_Par (lista):
    ind = 0
    tam = len(lista)
    soma = 0

    while ind < tam:
        if lista[ind] %2 == 0:
            soma = soma + lista[ind]
        ind += 1
    return soma
print(soma_Lista_Par([1, 2, 3, 4, 5, 6, 8]))'''

# Questão 5

'''def num_lista (lista, num):
    indice = 0
    while indice < len(lista):
        if num == lista[indice]:
           return True
        indice += 1
    return False

print(num_lista([1,2,3], 4))'''

# Questão 6

'''def soma_lista(lista1, lista2):
    soma1 = sum(lista1)
    soma2 = sum(lista2)
    if soma1 > soma2:
        return True
    return False

print(soma_lista([10, 20, 30, 50], [10, 30]))'''

# Questão 7

'''from math import factorial

def lista_fatorial (lista):
    indice = 0
    fatorial = 0
    while indice < len(lista):
        fatorial = factorial(lista[indice]) 
        print(fatorial)   
        indice += 1
    return fatorial
lista_fatorial([2, 4, 5])'''

# Questão 8

'''from statistics import median
from statistics import mean

def media_notas (nota):
    indice = 0
    media = 0
    mediana = 0
    verificador = 0
    while indice < len(nota):
        verificador = nota[indice]
        if verificador < 0 or verificador > 10:
            return
        indice += 1
    mediana = median(nota)
    media = mean(nota)
    return [mediana, media]
print(media_notas([10, 9.5, 4.5, 5.5, 8.5, 11]))'''

# Questão 9

'''def prova(questoes):
    indice = 0
    gabarito = ['A', 'A', 'C', 'E', 'D', 'B', 'C', 'E', 'B', 'D']
    verificador1 = 0
    verificador2 = 0
    acertos = 0
    while indice < len(questoes):
        verificador1 = questoes[indice]
        verificador2 = gabarito[indice]
        if verificador1 == verificador2:
            acertos += 1
        indice += 1
    return acertos
print(prova(['A', 'A', 'C', 'E', 'D', 'B', 'C', 'E', 'B', 'D']))'''

# Questão 10

'''def polindromo(palavra):
    lista = palavra
    indice = len(lista) -1
    contador = 0
    indice2 = 0
    contador2 = 0
    verificador = 0
    while indice >= 0:
        contador = lista[indice]
        if indice2 < len(lista):
            contador2 = lista[indice2]
            if contador == contador2:
                verificador += 1
                if verificador == len(lista):
                    return True
        indice2 += 1
        indice -= 1
    return False

print(polindromo('radar'))'''

# Questão 11

def elementos(palavra):
    indice = 0
    verificador = 0
    vogal = 0
    consoante = 0
    num = 0

    while indice < len(palavra):
        verificador = palavra[indice]
        if verificador in 'aeiou':
            vogal += 1
        elif '0' <= verificador <= '9':
            num += 1
        elif 'a' <= verificador <= 'z':
            consoante += 1
        indice += 1
    return [vogal, consoante, num]
print(elementos('fabricio123'))
