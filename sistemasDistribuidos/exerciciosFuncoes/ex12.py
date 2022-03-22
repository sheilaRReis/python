# Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com 
# os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn 
# ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres 
# serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
import random
def shuffleWord(word,upper):
    shuffled_word = str(random.choices(word,k=len(word)))
    if upper :
        return shuffled_word.upper()
    else:
        return shuffled_word.casefold()


def main():
    input_string = input("Informe uma string qualquer: ")
    new_word = shuffleWord(input_string,True)
    print(new_word)

main()