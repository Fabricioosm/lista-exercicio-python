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

from ProxPrimo import primo

lista = [2, 5, 7, 9, 4, 6, 8, 11] 
acu_primo = 0
i = 0
tam = len(lista)

while i < tam:
    if primo(lista[i]):
        acu_primo += 1
    i += 1
print(acu_primo)