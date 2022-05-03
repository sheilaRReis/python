# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor. 
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para 
# gerar numeros aleatórios, simulando os lançamentos dos dados.
import random
def throwDice():
    dice_values      = [1,2,3,4,5,6]
    list_dice_throws = list()
    for i in range(0,100,1):
        list_dice_throws.append(random.choice(dice_values))

    return list_dice_throws

list_throws = throwDice()
# print(list_throws)
print(f"O número 1 foi sorteado {list_throws.count(1)} vezes.")
print(f"O número 2 foi sorteado {list_throws.count(2)} vezes.")
print(f"O número 3 foi sorteado {list_throws.count(3)} vezes.")
print(f"O número 4 foi sorteado {list_throws.count(4)} vezes.")
print(f"O número 5 foi sorteado {list_throws.count(5)} vezes.")
print(f"O número 6 foi sorteado {list_throws.count(6)} vezes.")
