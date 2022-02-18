import random

def play() :
    user = input(f"Escolha entre: (R) pedra, (P) papel, ou T(tesoura): ").capitalize()
    computer = random.choice(['R', 'P', 'T']).capitalize()

    if user == computer:
        print ("Empate!")
    elif ( (user=="R" and computer=="T") or (user=="T" and computer=="P") or (user=="P" and computer=="R") ) :
        print("Parabéns, você venceu!")
    else:
        print("Ha-há! Você perdeu, otário!")

    print (f"Seu palpite: {user} Palpite do PC: {computer}")

play()