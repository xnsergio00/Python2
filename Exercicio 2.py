"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas
"""

vendas = [0, 0, 0, 0, 0]  # 100 200 300 200 125
ilhas = ['Faial', 'Pico', 'S. Jorge', 'Graciosa', 'Terceira']
total = 0
menor = 0
maior = 0

validar = True
while validar:
    for x in range(0, len(ilhas)):
        vendas[x] = int(input(f'Vendas {ilhas[x]}: '))
        if vendas[x] > maior:
            maior = vendas[x]
        total += vendas[x]
    menor = vendas[0]

    for x in range(0, len(vendas)):
        if vendas[x] < menor:
            menor = vendas[x]
    # print(vendas)
    print(f'Total de vendas: {total}')
    print(f'A menor venda é: {menor}')
    print(f'A maior venda é: {maior}')
    print(f'A média é: {total / len(ilhas)}')
validar = False

"""
defeclarar_lista(casas):
    vendas = []
    for x in range(casas):
        vendas.append(0)
    return vendas

if __name__ == '__main__':
    vendas = declarar_lista(5)
    print(f'vendas={v}')
    """
