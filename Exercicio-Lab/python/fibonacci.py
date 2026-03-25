user = int(input('Digite um número maior que zero: '))
contador = 0
numeroAnt = 0
numeroAtual = 0
novoNumero = 0


while contador < user:
    if contador <= 1:
        numeroAnt = contador + numeroAnt
        print(f'{numeroAnt} ', end='')
    if contador >= 2:
        novoNumero = numeroAnt + numeroAtual
        numeroAtual = numeroAnt 
        numeroAnt = novoNumero
        print(f'{novoNumero} ', end='')
    contador += 1
  

