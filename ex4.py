"""
4. Faça um algoritmo que verifica se um número inteiro informado pelo usuário é múltiplo de 3, utilizando o match-case
"""

n = int(input('Digite um número: '))

sim = False
if n % 3 == 0:
    sim = True

match sim:
    case True:
        print('É múltiplo de 3')
    case _:
        print('Não é múltiplo de 3')
