# Escreva um programa que retorna a área e o perímetro de um quadrado qualquer.
valid_input = False
while not valid_input :

    try:
        square_input = float(input("Qual o tamanho de um dos lados do quadrado, em centímetros?").strip().replace(",", "."))
    except ValueError:
        print("Valor inválido! Tente novamente")
        valid_input = False
    else:
        print(f"Área = {pow(square_input,2)} cm²")
        print(f"Perímetro = {square_input*4} cm²")
        valid_input = True

    