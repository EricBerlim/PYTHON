print('====== DESAFIO 010 ======')
real = float(input('Quantos reais você têm? R$'))
dolar = real / 5.40
euro = real / 6.56
iene = real / 0.052
print('Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f} ou ¥{:.2f}'.format(real, dolar, euro, iene))