#DISTÂNCIA DA VIAGEM EM KM E PREÇO DA PASSAGEM
distância = float(input('Qual é a distância da viagem? '))
print('Você está prestes a iniciar uma viagem de {}Km/h.'.format(distância))

#versão normal abaixo:
'''if distância <= 200:
    preço = distância * 0.50
else:                        
    preço = distância * 0.45'''

#versão simplificada abaixo:
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preço))
