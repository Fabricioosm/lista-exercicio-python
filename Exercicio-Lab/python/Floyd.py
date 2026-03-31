user = int(input('Digite um número maior que 0: '))
contador = 1
num = 1

while contador <= user:
    contador_dois = 0
    while contador_dois < contador:
        print(f'{num} ', end='')
        num += 1
        contador_dois += 1
    print('')
    contador += 1

