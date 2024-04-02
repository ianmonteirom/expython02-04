"""
1. Uma loja fornece 10% de desconto para funcionários e 5% de desconto para clientes vips. Faça um programa que
calcule o valor total a ser pago por uma pessoa. O programa deverá solicitar o valor total da compra efetuada e um
código que identifique se o comprador é um cliente comum (1), funcionário (2) ou vip (3).
"""

vt = float(input('Valor total a ser pago: '))
cod = int(input('Código: '))
vf = 0

match cod:
    case 1:
        vf += vt
    case 2:
        porc = vt * 10 / 100
        vf += vt - porc
    case 3:
        porc = vt * 5 / 100
        vf += vt - porc

print(f'Valor total a pagar: R${vf}')
