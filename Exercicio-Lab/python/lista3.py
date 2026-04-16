'''num1 = int(input('digite um número:'))
num2 = int(input('digite um número:'))
valor = False
if num1 < num2:
    valor = True
print(f'{valor}')'''

'''num1 = int(input('digite um número:'))
num2 = int(input('digite um número:'))
valor = False
if num1 and num2 > 0:
    valor = True
print(f'{valor}') '''

'''num1 = float(input('digite um número:'))
valor = False
if num1 > 0 and num1 < 1:
    valor = True
print(f'{valor}')
'''
'''n1 = int(input('digite um número:'))
n2 = int(input('digite um número:'))
n3 = int(input('digite um número:'))
valor = False
if (n1 != n2) and (n2 != n3) and (n1 != n3):
    valor = True
print(f'{valor}')'''

'''n1 = int(input('digite um número:'))
n2 = int(input('digite um número:'))
n3 = int(input('digite um número:'))
valor = False
if (n1 < n2) and (n2 < n3) and (n1 < n3):
    valor = True
print(f'{valor}')'''

'''n1 = int(input('digite um número:'))
valor = False
if n1 %2 == 0:
    valor = True
print(f'{valor}')'''

'''n1 = int(input('digite 4 números:'))
numIsolado = n1 % 100 #aqui ele separa o numero no meio por ',' 12,34 ou seja descarta oq vem antes da virgula
penDigito = numIsolado // 10 #descrta oq vem depois 
valor = False
if penDigito %2 == 1:
    valor = True
print(f'{valor}')'''

'''n1 = input('digite 4 números:')
if len(n1) < 3:
    print(f"O valor {n1} deve ter no minimo 3 caracters")
else:
    valor = list(n1) 
    teste = int(valor[-2])
    print(teste)
    if teste %2 == 1:
        print(True)
    else:
        print(False)'''