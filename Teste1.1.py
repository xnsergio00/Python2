def com_for(n1, n2):
    soma = 0
    for x in range(0, (n2 - n1) + 1):
        soma += n1 + x
        print(soma)
    return soma


def com_while(n1, n2):
    soma = 0
    x = 0
    while x < (n2 - n1) + 1:
        soma += n1 + x
        x += 1
    return soma


if __name__ == '__main__':
    num1 = 0
    num2 = 0
    func = '0'
    while True:
        try:
            num1 = int(input('Primeiro número? '))
            break
        except ValueError:
            print('Tem de ser um número.')
            continue
    while True:
        try:
            num2 = int(input('Segundo número? '))
            if num1 > num2:
                print(f'O primeiro({num1}) número não pode ser maior que o segundo número({num2}).')
                continue
            break
        except ValueError:
            print('Tem de ser um número.')
            continue

    while func == '0':
        func = input('Usar com_for ou com_while? ')
        if func == 'com_for':
            print(f'Resultado: {com_for(num1, num2)}')
            break
        elif func == 'com_while':
            print(com_while(num1, num2))
            break
        else:
            print('Erro, a função deve ser com_for ou com_while.')
            func = '0'