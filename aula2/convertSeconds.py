# Escreva um programa que recebe um valor em segundos e retorna em horas e minutos
valid_input = False
while not valid_input :

    try:
        seg_input = float(input("Informe um valor em segundos: ").strip().replace(",", "."))
    except ValueError:
        print("Valor inválido! Tente novamente")
        valid_input = False
    else:
        min_input = seg_input/60
        hour_input = min_input/60
        print("{:.2f} segundos equivalem a: {:.2f} minutos, ou {:.2f} hora(s)".format(seg_input, min_input, hour_input))

        valid_input = True