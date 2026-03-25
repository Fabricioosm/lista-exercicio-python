user = int(input('Digite um número: '))
contador = user // 2 
div = 1

while contador >= 1 and div <=2:
    if user % contador == 0:
        div += 1
    contador -= 1
if div == 2:
    print(f"{user} é um numero primo")
else:
    print(f"{user} não é um número primo")
