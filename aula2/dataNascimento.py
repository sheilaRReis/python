# Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de suaidade atual.
import datetime
valid_input = False
while not valid_input :
    try:
        age_input = int(input("Qual sua idade? ").strip())
    except ValueError:
        print("Valor inválido! Tente novamente")
        valid_input = False
    else:
        currentTime = datetime.datetime.now()
        currentYear = currentTime.year
        print(f"Você nasceu no ano de: {currentYear - age_input} ")