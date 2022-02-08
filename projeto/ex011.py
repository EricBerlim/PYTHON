larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))
area = larg * altu
tinta = area / 2

print('Dimensão de {}x{} e área de {}m².'.format(larg, altu, area))
print('Para pintar a parede, você precisará de {}l de tinta.'.format(tinta))
