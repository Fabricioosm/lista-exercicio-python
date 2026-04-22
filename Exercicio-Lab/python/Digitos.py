numero = int(input())
soma = 0

if numero < 0:
    numero = numero * -1

while numero > 0:
    numero = numero // 10
    soma += 1
print(soma)