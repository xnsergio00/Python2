def confor(n1, n2):
    soma = 0
    for x in range(0, (n2 - n1) + 1):
        soma += n1 + x
        print(soma)
    return soma

def conwhile(n1, n2):
    soma = 0
    x = 0
    while x < (n2 - n1) + 1:
        print(soma)



if __name__ == '__main__':
    n1 = int(input('1º número'))
    n2 = int(input('2º número'))
    numeros = (n1, n2)
    if n2 <= n1:
        print(f'erro')
    else:
        pergunta = (input('for | while'))
        while pergunta == 'while':
            soma = n1 + n2
            print(f'soma é {soma}')
            break
        while pergunta == 'for':
            soma = n1 + n2
            print(f'soma é {soma}')
            break


