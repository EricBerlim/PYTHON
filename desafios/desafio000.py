from random import randint
num = int(randint(0, 10))
palpite = 0
tentativas = 0
while palpite != num:
    palpite = int(input('[1;35mSeu palpite: \033[m'))
    tentativas += 1
    if palpite == num:
        print('\033[1;32mACERTOU! Placar: %i\033[m' % tentativas)
    elif palpite < num:
        print('\033[1;34mChute um valor MAIOR\033[m')
    else:
        print('\033[1;31mChute um valor MENOR\033[m')
print('Fim do jogo')
