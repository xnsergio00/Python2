"""
Primeiro num
Segundo num
For ou While | comfor(num1, num2) -- comwhile(num1, num2)
Soma
O 2 num tem que ser maior que o primeiro
Temos que ter somente numeros
"""


def aritmetica(num1, num2, op='+'):
        total = 'Código de operação inválido'
        if op == '+':
            total = num1 + num2
            return total
        if __name__ == '__main__':
            continuar = 's'
            while continuar == 's':
                num1 = float(input('Insira o 1º número'))
                num2 = float(input('Insira o 2º número'))
                operacao = input('Insira a operação [+] ')
                print(f"Olá {num1} {operacao} {num2} = {aritmetica(num1, num2, operacao)}")
                continuar = input('Repetir [s | n]? ')
                if continuar == 'n':
                    break



