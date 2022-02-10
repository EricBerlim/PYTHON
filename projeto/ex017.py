import math

catV = float(input('Comprimento do cateto oposto: '))
catH = float(input('Comprimento do cateto adjacente: '))
hipo = math.hypot(catV, catH)

print('A hipotenusa vai medir: {:.2f}'.format(hipo))
