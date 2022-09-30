"""
Lista Num (5 cases)
# Outra maneira de fazer o organizador de (lista)

Troquei = True
while troque:
troquei = false
for x in range(4):
if vendas [x] > vendas [x + 1]:
troquei = true
"""

import random


def get_random(ini, fim):
    return random.randrange(ini, fim + 1)


if __name__ == '__main__':
    nums = [0, 0, 0, 0, 0]
    estrela = [0, 0]
for y in range(5):
    for x in range(len(nums)):
        while True:
            onumero = get_random(1, 50)
            if onumero not in nums:
                nums[x] = onumero
            break

    for x in range(len(estrela)):
        while True:
            onumero = get_random(1, 12)
            if onumero not in estrela:
                estrela[x] = onumero
                break
        print(f' Os 5 numeros: {nums}')
        print(f' As 2 estrelas: {estrela}')

