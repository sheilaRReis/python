# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será 
# mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá 
# uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada
# na tela, informando se o usuário ganhou ou perdeu o jogo.
import random

words_file  = open("words.txt")
linhas      = words_file.readlines()
list_words  = list()

for linha in linhas:
    list_words = linha.split(",")

selected_word          = random.choice(list_words)
random_word_shuffled   = random.sample(selected_word, len(selected_word))

for letra in random_word_shuffled:
    print(letra, end=" ")
print("", end="\n")

for i in range(0,6,1):
    user_guess = input(f"Digite seu {i+1}º palpite: ").strip().lower()
    if(user_guess == selected_word):
        print("Parabéns! Você acertou!")
        break
    else:
        print("Palpite incorreto!")
        if(i==5):
            print("Você não tem mais palpites!")
            print(f"A resposta correta era {selected_word}")


