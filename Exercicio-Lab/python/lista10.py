# Questão 1

'''import random

def aleatorio(num):
    n_aleatorio = random.sample(range(1, 100,), num)
    return n_aleatorio
print(aleatorio(10))'''

# Questão 2

'''lista = [1, 2, -3, -4, 5, -6, 7, 8, -9]
novaLista = []
num = 0
modulo = 0
indice = 0'''

'''while indice < len(lista):
    num = lista[indice]
    if num < 0:
       modulo = num * -1
       num = modulo
    novaLista.append(num)
    indice += 1
print(novaLista)'''

# Questao 3

'''lista = [10, 50, 89, 20]
num_max = max(lista)
indice = 0
div = 0
num = 0
lista_num_max = []
while indice < len(lista):
    num = lista[indice]
    div = num / num_max
    lista_num_max.append(div)
    indice += 1
print(lista_num_max)'''

# Questão 4

'''def primo(num):
    contador = num // 2 
    div = 1
    while contador >= 1 and div <= 2:
        if num % contador == 0:
            div += 1
        contador -= 1
    numero = div == 2
    return numero'''

'''def lista_primo(lista): 
    indice = 0
    num_lista = 0
    nova_lista_primo = []
    while indice < len(lista):
        num_lista = lista[indice]
        if primo(num_lista):
            nova_lista_primo.append(num_lista)
        indice += 1
    return nova_lista_primo

print(lista_primo([1, 2, 3, 4, 5, 6, 7, 8, 9]))'''

# Questão 5

'''def proximo_primo(quant, num_partida):
    new_list_primo = []
    next_primo = num_partida + 1
    while len(new_list_primo) < quant:
        if primo(next_primo):
            new_list_primo.append(next_primo)
        next_primo += 1
    return new_list_primo

print(proximo_primo(3, 3))'''

# Questão 6

def mult_lista(num1, num2):
    indice = 0
    mult = 0
    nova_lista = []

    while indice < len(num1) or indice < len(num2):
        if indice >= len(num2):
            nova_lista.append(num1[indice])
        elif indice >= len(num1):
            nova_lista.append(num2[indice])
        else:
            lista1 = num1[indice]
            lista2 = num2[indice]
            mult = lista1 * lista2
            nova_lista.append(mult)
        indice += 1
    return nova_lista

print(mult_lista([2, 4, 6, 8], [1, 3, 5, 7, 9]))
    
