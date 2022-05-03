import random
from words import words
import string

def get_valid_word(words) : 
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
 

def hangman() :
    word         = get_valid_word(words)
    word_letters = set(word)
    alphabet     = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10

    while len(word_letters) > 0 and lives > 0 :
        print(f"Você possui {lives} vida(s)")
        
        if len(used_letters) > 0 :
            print("Letras usadas: ", " ".join(used_letters))

        word_list    = [letter if letter in used_letters else "-" for letter in word]
        print("Palavra: ", " ".join(word_list))
        
        user_letter_input = input('Digite uma letra: ').upper()

        if user_letter_input in alphabet - used_letters:
            used_letters.add(user_letter_input)
            if user_letter_input in word_letters:
                word_letters.remove(user_letter_input)
            else : 
                lives = lives - 1
                print(f"A letra {user_letter_input} não está nesta palavra")
        elif user_letter_input in used_letters :
            print('Você já chutou esta letra. Tente novamente!')
        else:
            print('Você digitou um caracter inválido.')
    if lives == 0 :
        print(f"Ha-há! Você morreu. A palavra era: {word}")
    else:
        print("Parabens!Você adivinhou a palavra!")
        

hangman()