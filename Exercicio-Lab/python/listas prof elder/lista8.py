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

def intervalo (inicio, fim, numTeste, opcional=True):
    if not opcional:
         
    if numTeste < inicio or numTeste > fim:
        return False
    else:
        numTeste >= inicio and numTeste <= fim
        return True

teste = intervalo(3, 6, 5) 
print(teste)




    