user = float(input('Digite um número maior que 0: '))
contador = 0
div = 0
soma = 0
fatorial = 0

while contador < user:
    if contador == 0:
        fatorial = 1
    if contador > 0:
        fatorial = fatorial * contador
    div = 1 / fatorial
    soma = soma + div
    contador += 1
   
print(soma)
    
