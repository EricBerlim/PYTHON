real = float(input('Valor a ser convertido: R$'))
dolar = real / 5.26
euro = real / 6.00
iene = real / 0.046

print('########## CONVERSOR ##########')
print('Com R${} você pode ter U${:.2f}'.format(real, dolar))
print('Com R${} você pode ter €{:.2f}'.format(real, euro))
print('Com R${} você pode ter ¥{:.2f}'.format(real, iene))
