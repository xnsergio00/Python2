def divisores(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros += 1  # zeros = zeros +1
    return zeros


if __name__ == "__main__":
    continuar = 's'
    while continuar == 's':
        numero = int(input('Insira um número'))
        if divisores(numero) == 2:
            print(f"0 número {numero} é primo. ")
        else:
            print(f'O número {numero} mão é primo.')
        continuar = input('Repetir [s | n]? ')
    print(f'Adeus !')
