""" 1- obter nota via entrada de usuário, P1, P2, TP(trabalho pratico), ME(media dos exercicios) 0 <= nota <= 10
    2- obter quantidade total de aulas via user que deve ser no intervalo de 14 <= total <= 16
    3- obter quantidade de presença do aluno via user deve ser 75%  se não frequencia insuficiente 
    4- se o aluno ficar em recuperação tambem deve obter essa bota NF = (MF + REC) /2
    5- Todas as entradas precisam ser validadas para que a média e a frequência sejam analisadas
    6- caso não receba alguma entrada apresente: entrada invalida
    7- a media final deve ser calculada MF = MP X 0,7 + ME X 0,1 + TP X 0,2
    8- MP = (P1 + P2)/2
    9- se a media final for entre 3,0 e 5,5
""" 
p1 = float(input())
p2 = float(input())
tp = float(input())
me = float(input())
total_aula = float(input())
pa = float(input())


if p1 == False or p2 == False or tp == False or me == False or total_aula == False or pa == False:
    print("entrada ivalida")

