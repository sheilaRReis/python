# Lista de exercícios para ajudar na fixação do conteúdo
#  1. Peça ao usuário que entre com 3 valores inteiros e retorne a soma dele
invalid_input = False
while not invalid_input:
    try:
        input_v1 = int(input("Digite um valor inteiro: "))
        input_v2 = int(input("Digite o 2º valor: "))
        input_v3 = int(input("Digite o 3º valor: "))
    except ValueError:
        print("Valor inválido!")
        invalid_input = True
    else:
        sum = input_v1 + input_v2 + input_v3
        print(f"{input_v1} + {input_v2} + {input_v3} é igual a {sum}")