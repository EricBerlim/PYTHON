# Diária custa 60 e Km rodado custa 0.15

dias = int(input('Alugar por quantos dias? '))
km = float(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(total))
