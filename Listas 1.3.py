def factorial(numero):
    fact = 1
    if numero < 0:
        print('Numeros negativos sao inválidos.')
    else:
        for n in range(1, numero + 1):
            fact = fact * n

    return fact

if __name__ == '__main__':
    numero = int(input('Insira o numero:'))
    print(f'A fatorial do numero {numero} é {factorial(numero)}')
