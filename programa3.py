
def par(numero):
    if numero % 2 == 0:

        return True
    else:
        return False


if __name__ == "__main__":
    nome = input('Como te chamas?')
    continuar = 's'
    while continuar == 's':
        num = int(input('Insira um número'))
        if par(num):
            print(f'O número {num} é par.')
        else:
            print(f'O número {num} é impar.')
        continuar = input('Repetir [s | n]? ')
    print(f'Adeus {nome}!')














