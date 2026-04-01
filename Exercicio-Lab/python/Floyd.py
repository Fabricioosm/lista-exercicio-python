user = int(input('Digite um número maior que 0: '))
contador = 1
num = 1

while contador <= user:
    contador_dois = 0
    while contador_dois < contador:
        # print(f'{num} ', end='')
        if num < 100 and num < 10:
            print(f'00{num} ', end='')  
        if num < 100 and num >= 10:
            print(f'0{num} ', end='')
        elif num >= 100:
            print(f'{num} ', end='')
        

        num += 1
        contador_dois += 1
    print('')
    contador += 1

