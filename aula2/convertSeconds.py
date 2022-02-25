# Escreva um programa que recebe um valor em segundos e retorna em horas e minutos
valid_input = False
while not valid_input :

    try:
        seconds = int(input("Informe um valor em segundos: ").strip().replace(",", "."))
    except ValueError:
        print("Valor inválido! Tente novamente")
        valid_input = False
    else:
        minutes = int(seconds/60)
        hours = int(minutes/60)

        remaining_minutes = (seconds/60-minutes) * 60
        remaining_seconds = (minutes/60-hours) * 60
        print("{} segundos equivalem a: {} minutos, ou {} hora(s)".format(seconds, minutes, hours))

        valid_input = True