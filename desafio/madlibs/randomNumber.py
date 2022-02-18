from calendar import c
import random
from statistics import correlation

def user_guess(x):
    randomNumber = random.randint(1, x)
    user_guess    = 0
    while user_guess != randomNumber:
        user_guess    = int(input(f"Digite seu palpite, entre 1 e {x}: "))
        if user_guess > randomNumber :
            print(f"Tente novamente. O seu palpite de {user_guess} é maior que o número aleatório")
        elif user_guess < randomNumber :
            print(f"Tente novamente. O seu palpite de {user_guess} é menor que o número aleatório")

    print(f"Resposta correta! Número aleatório: {randomNumber}. Seu palpite: {user_guess}")

def computer_guess(x) :
    low  = 1
    high = x
    user_feedback = ''
    random_number = random.randint(low, high)

    while user_feedback!= "E":
        if low != high:
            pc_guess = random.randint(low, high)
        else :
            pc_guess = low

        user_feedback = str(input(f"{pc_guess} é maior (h), menor (l) ou igual (e) a {random_number}?")).capitalize()

        if user_feedback == "H":
            high = pc_guess - 1
        elif user_feedback == "L" :
            low = pc_guess + 1

    print(f"Resposta correta! Palpite do PC: {pc_guess}")


computer_guess(10)