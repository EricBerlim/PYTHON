#RADAR ELETRÔNICO
velocidade = float(input('Velocidade do veículo: '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de 80 Km/h.')
    multa = (velocidade - 80) * 7 #ultrapassou de 80|vezes 7 reais para cada km acima
    print('Você deverá pagar uma multa de R${:.2f}.'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
