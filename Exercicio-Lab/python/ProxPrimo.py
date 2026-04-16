def primo(numero):
    contador = numero // 2
    div = 1
    while contador >= 1 and div <= 2:
        if numero % contador == 0:
            div += 1
        contador -= 1
    numPrimo = div == 2
    return numPrimo

def proxprimo (num):
    next_primo = num + 1
    while not primo(next_primo):
        next_primo += 1
    return next_primo

print(proxprimo(int(input('Digite um numero maior que zero: '))))

