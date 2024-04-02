"""
5. Faça um algoritmo que solicite o código da palestra de um evento e exiba o local em que ela será realizada, conforme
a tabela a seguir:
"""

cod = int(input('Informe o código da palestra: '))
pa = ['Linux', 'Banco de Dados', 'Windows Server', 'Lógica e Programação']
palestra = ''
loc = ['1', '2', '3', 'Principal']
local = ''

match cod:
    case 1:
        palestra += pa[0]
        local += loc[0]
    case 2:
        palestra += pa[1]
        local += loc[1]
    case 3:
        palestra += pa[2]
        local += loc[2]
    case 4:
        palestra += pa[3]
        local += loc[3]
    case _:
        print('Informe o código correto!')

if cod in (1, 2, 3, 4):
    print(f'PALESTRA: {palestra}\n'
          f'AUDITÓRIO: {local}')
