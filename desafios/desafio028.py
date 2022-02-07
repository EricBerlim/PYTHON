#JOGO DE ADIVINHAR UM NÚMERO
from random import randint #vai randomizar um nº inteiro
from time import sleep #faz o pc dormir por segundos
computador = randint(0, 5) #faz o pc "pensar" em um nº
print('-=-' * 20) #apenas enfeite
print('Pensei em um número entre 0 e 5! Tente adivinhar...')
print('-=-' * 20) #apenas enfeite
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2) #vai dormir por 2 segundos
if jogador == computador:
    print('PARABÉNS! Você venceu!')
else:
    print('GANNET! Eu pensei no número {} e não no número {}!'.format(computador, jogador))
