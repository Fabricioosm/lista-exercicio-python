'''n1 = int(input('digite um número:')) # é o limite onde o while looping, que vai ser digitado pelo usuario, basicamente ele quer saber quamtos númerod impares tem até esse número digitado
contador = 0 # vai mostrar os numeros 
if n1 > 1: #vai executar a ação somente se o número for maior que 1
    while contador <= n1: # enquanto o contador for menor ou igual ao numero digitado ele executa a condição de looping 
        if contador %2 == 1: # aqui ele vai fazer a verificação dos números impares que ele vai mostrar na tela
           print(contador) # vai mostrar na tela 
        contador = contador + 1 # ele é oq faz o 0 virar 1, o 1 virar 2...'''

'''num = 20
while num > 0:
    print(num)
    num = num - 1'''

'''num1 = int(input('Digite um número: '))
contador = 1
while contador <= 10:
    res = num1 * contador
    print(f'{num1} x {contador} = {res}')
    contador = contador + 1'''

'''limiteI = int(input('digite um número:'))
limiteS = int(input('digite um número:'))
soma = 0 

if limiteI <= limiteS: 
    while limiteI <= limiteS: 
        soma = soma + limiteI
        print(soma)
        limiteI += 1'''

'''user = int(input('Digite um número:'))
multiplicador = 0
while multiplicador <= user:
    res = multiplicador * user
    print(res)
    multiplicador += 1'''

'''n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
mult = 1
while n1 <= n2:
    mult = mult * n1
    print(mult)
    n1 += 1'''

'''user = int(input('Digite um número: '))
soma = 0
contador = 0

while user != 0:
    soma = soma + user
    contador += 1
    media = soma / contador
    user = int(input('Digite um número: '))
print(f'soma= {soma}, media= {media}, contador={contador}')'''

'''user = int(input('Digite um número: ')) # aqui ele pede pro usuario digitar um número
contador = 0 # o contador serve para acrescenatar o valor  e verificar se é um numero divisivel por mil
divPorMilQuant = 0 # quantidade de numeros que são divisiveis por 1000

while user != 0 and (user < 1 or user > 9): # aqui ele verifica se o numero é diferente de 0 e maior que 1 ou menor que 9, aqui ele precisa colocar o diferente de zero para poder disparar o outro erro que a função pede
    user = int(input('ERRO, Digite um número entre 1 e 9: ')) # se o valor for false ele retorna o erro

if user == 0: # aqui ele verifica se o valor é igual a zero se ele for igual a zero ele dispara o erro 
    print('programa encerrado sem realizar calculo') 
elif user >=1 and user <=9: # aqui ele verifica se o numero é entre 1 e 9
    while contador != 1000: # aqui ele vai somar mais um até que o número do contador chega em 999
        if contador % user == 0: # aqui ele verifica se o numero que o contador esta é divisivel pelo numero do usuario
            divPorMilQuant += 1 # aqui vai ser o resultado dessa divisao caso ele for divisivel ele acrescenta 1
        contador +=1 # aqui é para ele ir fazendo o looping até chegar em 999
    print(divPorMilQuant)'''


user = int(input('Digite um número: ')) 
contador = 0
res = ''
letra = 'A'

while 0 < user:
    res = res + letra 
    user -= 1
    contador += 1

    if contador == 3:
        contador = 0
        if letra == "A":
            letra = "B"
        elif letra == "B":
            letra = "C"
        elif letra == "C":
            letra = "A"
print(res)

  
