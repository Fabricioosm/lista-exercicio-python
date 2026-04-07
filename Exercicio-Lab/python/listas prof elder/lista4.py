'''lado1 = int(input('Digite um número:'))
lado2 = int(input('Digite um número:'))
lado3 = int(input('Digite um número:'))
if lado1 < lado2 + lado3:
    print('isso é um triângulo')
else:
    print('não existe um triângulo')'''

'''n1 = float(input('digite um número:'))
n2 = float(input('digite um número:'))
if n1 < n2:
    print(n1)
elif n2 < n1:
    print(n2)
else:
    n1 == n2
    print('valores iguais')'''

'''n1 = float(input('digite um número:'))
n2 = float(input('digite um número:'))
n3 = float(input('digite um número:'))
if  (n1 > n2 and  n1 > n3):
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
elif n3 > n1 and n3 > n2:
    print(n3)
else:
    n1 == n2 == n3 and n1 == n3
    print('valores iguais')'''

'''cat1 = float(input('digite o cateto 1:'))
cat2 = float(input('digite o cateto 2:'))
if (cat1 < 0) or (cat2 < 0):
    print("O calculo não pode ser realizado pois o valor é negativo")
else:
    hip = ((cat1**2) + (cat2**2))**0.5
    print(hip)'''

'''n1 = int(input('digite um número:'))
n2 = int(input('digite um número:'))
if n1 > n2:
    print(f" O maior valor é o {n1}")
else:
    n2 > n1
    print(f"O maior valor é o {n2}")'''

'''n1 = float(input('digite um número:'))
if n1 > 0 and n1 < 1:
    print(f'o valor {n1} esta entre 0 e 1')'''

'''vogal = input('Digite uma letra:')
if (vogal == 'a') or (vogal == 'e') or (vogal =='i') or (vogal =='o') or (vogal =='u'):
    print(f' Sim a letra {vogal} é uma vogal')
else: 
    print(f'A letra {vogal} não é uma vogal')'''


'''n1 = int(input('digite um número:'))
n2 = int(input('digite um número:'))
if n1 %n2 == 0:
    print(f'sim {n1} é multiplo de {n2}')'''

'''valor = int(input('Digite o valor da compra:'))
if valor >= 6999:
    porcentagem = 0.15 * valor
    desconto1 = valor - (valor *(15/100))
    print(f'Você teve um desconto de 15%({porcentagem}) o valor final da sua compra é {desconto1}')
else:
    porcentagem2 = 0.05 * valor
    desconto2 = valor - (valor *(5/100))
    print(f'Você teve um desconto de 5%({porcentagem2}) o valor final da sua compra é {desconto2}')'''


'''n1 = int(input('digite um número:'))
n2 = int(input('digite um número:'))
if n1 > n2:
    print(f'{n1} é o maior')
elif n2 > n1:
    print(f'{n2} é o maior')
else:
    n1 == n2
    print(f'{n1} e {n2} são iguais')'''

'''altura = float(input('Digite sua altura:'))
idade = int(input('Digite sua idade:'))
horas = int(input('Que horas é seu voo?'))
peso = int(input('Qual seu peso?'))

if altura >= 1.75 and idade >=22 and idade <=40 and horas > 1600 and peso >= 65 and peso <= 95 :
    print('Você atende todas as condições, está apto para entrar no curso')
else:
    print('Você não atende todas as condições, você não está apto para entrar no curso')'''

'''caixa = int(input('Digite o valor que deseja sacar:'))
if caixa %5 == 0:
    v50 = caixa // 50 # quantas notas de 50 ele vai dar, ou sela 135/50 = 2,7, a divisao inteira o resultado seria 2
    resto = caixa %50 # as notas que ainda faltam entregar, ou seja a sobra da divisao do valor divido por 50
    v10 = resto // 10
    resto = resto %10 
    v5 = resto // 5
    print(f'saque concluido, você recebeu {v50} de 50, {v10} notas de 10, {v5} notas de 5 ')
       
else:
   print('valor indisponivel')'''
