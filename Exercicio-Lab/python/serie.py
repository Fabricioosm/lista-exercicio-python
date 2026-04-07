user = int(input('Digite um número inteiro maior que 0: '))
contador = 1
MultDois = 2 
multTres = 1
MultQuatro = 1
resDois = 1
resTres = 7
resQuatro = 3


while contador < user or user >= 1:
    if contador == 1:
        MultDois = resDois * 2
        resDois = MultDois
        print(f'{MultDois},', end= '')
    elif contador == 2:
        print(f'{resTres},', end='')
        multTres = resTres* 3
        resTres = multTres
    elif contador == 3:
        print(f'{resQuatro},', end='')
        MultQuatro = resQuatro * 4
        resQuatro = MultQuatro
        contador = 0
    contador += 1
    user -= 1
  