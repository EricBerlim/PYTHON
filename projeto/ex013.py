salario = float(input('Salário atual: R$'))
aumento = salario + (salario * 15 / 100)

print('O salário atual de R${:.2f}, com 15% de aumento fica R${:.2f}'.format(salario, aumento))

