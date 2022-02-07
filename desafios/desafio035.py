#Cada reta tem que ser menor do que a soma dos outros 2
print('=-=' * 10)
print('ANALISADOR DE TRIÂNGULOS')
print('=-=' * 10)
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima PODEM FORMAR um triângulo!')
else:
    print('As retas acima NÃO PODEM FORMAR um triângulo!')
