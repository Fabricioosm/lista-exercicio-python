user = int(input('Digite um número: '))
par = 0 
impar = 0
novo_impar = 0
imparAnt = 0



while user >= 0:
    if user %2 == 0:
        par += 1
    if user %2 == 1:
        impar += 1
        imparAnt = user
    if user %2 == 1 and imparAnt > novo_impar:
        novo_impar = imparAnt
    user = int(input('Digite outro número: '))
    if impar == 0:
        novo_impar = 'nenhum'

print(f'{par},', end='')
print(f'{impar},', end='')
print(f'{novo_impar} ', end='') 