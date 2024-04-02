"""
2. Solicite a primeira letra do estado civil de uma pessoa ('S', 'C', 'V', 'D') e mostre uma mensagem com a sua descrição
('Solteiro', 'Casado', 'Viúvo', 'Divorciado'). Mostre uma mensagem de erro, se necessário (o algoritmo deve funcionar
para letras maiúsculas e minúsculas).
"""

ec = str(input('Primeira letra do estado civil: ')).strip().lower()

match ec:
    case 's':
        print('Solteiro')
    case 'c':
        print('Casado')
    case 'v':
        print('Viúvo')
    case 'd':
        print('Divorciado')
    case _:
        print('Digite uma letra válida!')
