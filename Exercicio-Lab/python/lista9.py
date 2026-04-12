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


    
