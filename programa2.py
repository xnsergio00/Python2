## Apresentar a os valores da nota em letra
##(A, 80-100; B, 60-79; C, 40-59; D, 20-39; E, 0-19)


if __name__ == "__main__":
    nome = input('Como te chamas?')

while True:
    nota = int(input('Insere a tua nota: '))

    if 80 <= nota <= 100:
        print('Tens A')

    if 60 <= nota <= 79:
        print('Tens B')

    if 40 <= nota <= 59:
        print('Tens c')

    if 20 <= nota <= 39:
        print('Tens D')

    if 0 <= nota <= 19:
        print('Tens E')

    if 0 < nota > 100:
        print('Número Inválido')

    continuar = input('Quer continuar? [s,n] ')
    if continuar == 'n':
        break

print(f'Adeus {nome}!')
