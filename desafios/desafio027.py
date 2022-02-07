#LER NOME COMPLETO MOSTRAR O 1 E ÚLTIMO NOME
#split = dividir o nome separando pelos espaços
n = str(input('Qual o seu nome completo? ')).strip()
nome = n.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome) - 1]))
#mostra o 'nome' na posição 'len' de 'nome' - 1
