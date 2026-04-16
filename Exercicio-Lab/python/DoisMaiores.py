def inputListaInteiros():
    return [int(ent) for ent in input().split()]

def dois_maiores():
    lista = inputListaInteiros()
    if len(lista) == 1:
        return f'{lista[0]}, nenhum'
    if lista[0] > lista[1]:
        maior = lista[0]
        segundo = lista[1]
    else:
        maior = lista[1]
        segundo = lista[0]
    num = 0
    contador = 2
    while contador < len(lista):
        num = lista[contador]
        if num > maior:
            segundo = maior
            maior = num
        elif num < maior and num > segundo:
            segundo = num
        contador += 1
    return f'{maior}, {segundo}'

print(dois_maiores())

    


