# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#   12376489
#   => 98467321

invalid_input = True
while(invalid_input):
    try:
        input_n = int(input("Digite um número inteiro positivo: ").strip())
        invalid_input = input_n<0
    except(ValueError):
        invalid_input = True
        print("Valor inválido! Tente novamente.")

str_numbers = str(input_n)
for i in range(len(str_numbers)-1, -1, -1):
    print(str_numbers[i], end="")