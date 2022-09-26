"""
1. Pede ao utilizador 2 números. O 2º número deve ser >= 1º
Mostra todos os números primos, que há entre o 1º e o 2º
Depois de mostrar os números diz quantos números primos havia.

2. Pede ao utilizador um número inicial
Pede ao utilizador um número que representa "Quantos"
Mostra aquela quantidade de números primos a partir do número inicial
"""
#1.
""""
def divisores(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros += 1  # zeros = zeros +1
    return zeros


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        ini = int(input('Insira o número inicial'))
        fim = int(input('Insira o número final'))
        primos = 0
        # Alterar o for para um while
        for n in range(ini, fim + 1):
            if divisores(n) == 2:
                primos += 1
        print(f'Entre {ini} e {fim} há {primos} de primos.')
        continuar = input('Repetir [s | n]? ')
    print(f'Adeus!')
"""

#2.





