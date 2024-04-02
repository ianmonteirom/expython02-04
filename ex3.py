"""
3. Faça um programa que receba um número, digitado pelo usuário e mostre o menu para selecionar o tipo de cálculo
que deve ser realizado. Exiba o resultado do cálculo efetuado.
1 - O dobro
2 - A metade
3 - 10% do número
"""

n = float(input('Digite um número: '))

print('1 - O dobro\n'
      '2 - A metade\n'
      '3 - 10% do número')

opcao = int(input('Selecione o tipo de cálculo: '))

match opcao:
    case 1:
        n *= 2
    case 2:
        n /= 2
    case 3:
        n = n * 10 / 100

print(n)

