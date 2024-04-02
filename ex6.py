"""
6. Faça um algoritmo que exiba um Menu com as opções de um cardápio de restaurante. O cliente deve escolher o
código do prato desejado e na sequência, informar se aceita pagar a gorjeta do garçom. Se o usuário aceitar, mostrar
o valor final (valor do prato + 10%), caso contrário, mostrar somente o valor do prato.
"""

print('MENU DO RESTAURANTE\n'
      '\n'
      'CÓDIGO     PRATO           VALOR\n'
      '1          Picanha         R$25,00\n'
      '2          Lasanha         R$20,00\n'
      '3          Strogonoff      R$20,00\n'
      '4          Bife Acebolado  R$15,00\n'
      '5          Pão com Ovo     R$5,00\n')

opcao = int(input('Prato desejado (informe o código): '))
garc = str(input('Aceita pagar a gorjeta do garçom? [S/N] ')).strip().lower()
valor = 0
gorj = 0

match opcao:
    case 1:
        valor += 25
    case 2 | 3:
        valor += 20
    case 4:
        valor += 15
    case 5:
        valor += 5

match garc:
    case 's':
        gorj += valor * 10 / 100

vt = valor + gorj

print(f'Total a pagar: R${vt}')
