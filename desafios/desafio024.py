#NOME DE UMA CIDADE E DIZER SE COMEÇA COM 'SANTO'
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')
