valor = float(input('Valor do produto: R$'))
desconto = valor - (valor * 5 / 100)

print('Custava R${:.2f}, mas com desconto de 5% fica R${:.2f}.'.format(valor, desconto))

