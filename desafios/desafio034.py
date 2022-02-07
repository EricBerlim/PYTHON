#SALÁRIO E AUMENTO | IF: OU ELSE:
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novosalário = salário + (salário * 15 / 100) #Aumento de 15%
else:
    novosalário = salário + (salário * 10 / 100) #Aumento de 10%
print('Quem ganhava R${:.2f} passa a ganhar {:.2f}.'.format(salário, novosalário))
