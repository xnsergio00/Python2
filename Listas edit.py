"""
Fazer alteração de soma entre os primeiros numeros das duas listas
"""


if __name__ == '__main__':
    vendas = [
        [10, 20, 30, 40, 50],
        [15, 25, 35, 45, 55]
    ]

    print(vendas)

    for venda in vendas:
        print(venda)
        for v in venda:
            print(v)

    x = 0  # número da lista
    y = 0  # número da coluna

    for x in range(2):
        total = 0
        for y in range(5):
            print(f'x = {x} y = {y}')
            total = vendas[0][y] + vendas[1][y]
            print(f'A soma entre a vendas [{0}][{y}] + a venda[{1}][{y}] = {total}')
            print(total)

    for x in range(2):
        print(x)

    for y in range(5):
        total = 0
        for x in range(2):
            total = vendas[0][y] + vendas[1][y]
            print(f'x={x} y={y}')
            print(total)


