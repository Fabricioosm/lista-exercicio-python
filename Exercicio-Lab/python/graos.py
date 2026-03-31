grao = 1
graoAtual = 1
soma = 0

while grao <= 64:
    soma = soma + graoAtual
    graoAtual = graoAtual * 2
    grao += 1    
print(f'soma = {soma} numero de grãos no quadro = {graoAtual / 2}')