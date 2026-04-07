#Questão 1

'''def intervalo (inicio, fim, numTeste):
    if numTeste < inicio or numTeste > fim:
        return False
    else:
        numTeste >= inicio and numTeste <= fim
        return True

teste = intervalo(3, 6, 5) 
print(teste)'''

#Questão 2

'''def intervalo (inicio, fim, numTeste,fechado=True):
    if not fechado:
        numFechado = numTeste > inicio and numTeste < fim
        return numFechado

    if numTeste < inicio or numTeste > fim:
        return False
    else:
        numTeste >= inicio and numTeste <= fim
        return True

teste = intervalo(3, 6, 6, False) 
print(teste)'''

# Questão 3

'''def nota (num = 0, num1 = 10, notaTeste = 0):
    nota = num <= notaTeste <=10
    return nota

teste = nota(notaTeste = -1)
print(teste)'''

'''def nota_valida(notaProva):
    return 0 <= notaProva <= 10

print(nota_valida(11))'''

# Questão 4

def fatorial(numero):
    acu = 1 
    while numero >= 1:
        acu = acu * numero
        numero -= 1
    return acu

#print(fatorial(5))

# Questão 5

'''def expressao (n, p):
    ene = fatorial(n)
    pe = fatorial(p)
    div = fatorial(n - p)

    res = ene / (pe * div)
    return res
print(expressao(7, 5))'''

# Questão 6 

'''def seqInfinita (num):
    if num <= 0:
        return None
    contador = 0
    div = 0
    soma = 0
    while contador < num:
        div = 1 / fatorial(contador)
        soma = soma + div
        contador += 1
    return soma

print(seqInfinita(9))'''

# Questão 7

'''def cosseno(num, x):
    if num <= 0:
        return None

    numPar = 0
    soma = 0
    contador = 0
    sinal = 1
    div = 0
    expoente = 0

    while contador < num:
        expoente = x ** numPar
        div = expoente / fatorial(numPar)
        soma = soma + (div * sinal)
        sinal = sinal * -1
        numPar += 2
        contador += 1
    return soma

print(cosseno(2, 0.1))'''

# Questão 8
            
def seno (num, x):
    if num <= 0:
        return None

    numImpar = 1
    sinal = 1
    contador = 0
    soma = 0
    div = 0
    expoente = 0

    while contador < num:
        expoente = x ** numImpar
        div = expoente / fatorial(numImpar)
        soma = soma + (div * sinal)
        sinal = sinal * -1
        numImpar += 2
        contador += 1
    return soma
print(seno(2, 0.1))
                  



    






    