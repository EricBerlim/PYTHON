print('====== DESAFIO 013 ======')
salário = float(input('Qual é o salário? R$'))
novo = salário + (salário * 15 / 100)
print('O salário, que era R${:.2f}, com 15% de aumento, passa a ser R${:.2f}'.format(salário, novo))
