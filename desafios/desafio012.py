print('====== DESAFIO 012 ======')
preço = float(input('Qual é o preço? R$'))
novo = preço - (preço * 5 / 100)
print('O preço com 5% de desconto ficará R${:.2f}'.format(novo))
