ilhas = ['Terceira', 'Pico', 'Faial', 'São Jorge', 'Graciosa']
tipos = ['Gasolina', 'Gasóleo']
vendas = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

totais = [0, 0, 0, 0, 0]

if __name__ == '__main__':
    # Obter input
    for x in range(len(vendas)):
        for y in range(len(vendas[x])):
            while True:
                try:
                    vendas[x][y] = int(input(f'Insira vendas de {tipos[x]} para a ilha {ilhas[y]}:'))
                    break
                except ValueError:
                    print(f'Insira um valor válido para vendas de {tipos[x]} na ilha {ilhas[y]}')
    for venda in vendas:
        print(vendas)

    # Imprimir vendas por tipo
    for x in range(len(vendas)):
        total = 0
        for y in range(len(vendas[x])):
            total += vendas[x][y]
        print(f'Total de vendas para {tipos[x]} = {total}')

        # Imprimir vendas por ilhas
        z = 0
        for y in range(len(vendas[z])):
            z += 1
            total = 0
            for x in range(len(vendas)):
                total += vendas[x][y]
            print(f'Total de vendas para {ilhas[y]} = {total}')
            totais[y] = total

        # Total de vendas

        total = 0
        for x in range(len(vendas)):
            for y in range(len(vendas[x])):
                total += vendas[x][y]
        print(f'Total de vendas = {total}')

        # Ilhas com vendas máximas

        maior = totais[0]
        menor = totais[0]
        for x in range(1, len(totais)):
            if totais[x] > maior:
                maior = totais[x]
            if totais[x] < menor:
                menor = totais[x]

        ilhas_maior = []
        ilhas_menor = []

        for x in range(len(totais)):
            if totais[x] == maior:
                ilhas_maior.append(ilhas[x])
            if totais[x] == menor:
                ilhas_menor.append(ilhas[x])

        print(totais)
        print(f'ilhas_maior = {ilhas_maior} = {maior}')
        print(f'ilhas_menor = {ilhas_menor} = {menor}')

        # Ilha que consumiu mais gasolina e a que consumiu mais gasoleo



