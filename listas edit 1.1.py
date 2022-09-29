"""
Imprimir 7 linhas total da gasolina, gasoleo e ilhas do grupo central
"""

if __name__ == '__main__':
    ilhas = ['Terceira', 'Pico', 'Graciosa', 'Faial', 'São Jorge']
    tipos = ['Gasolina', 'Gasoleo']
    vendas = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    pergunta = (input('[Gasolina | Gasoleo]'))
    if pergunta == 'Gasolina':
        valor1 = int(input('1º valor'))


