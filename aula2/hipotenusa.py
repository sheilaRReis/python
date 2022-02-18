#  Sejam a e b os catetos de um triângulo retângulo, onde a hipotenusa é obtida pela equação:
# Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa e imprima o resultado.

# Escreva um programa que retorna a área e o perímetro de um quadrado qualquer.
import math

valid_input = False
while not valid_input :
    try:
        input_a = float(input("Digite o valor do cateto a: ").strip().replace(",", "."))
        input_b = float(input("Digite o valor do cateto b: ").strip().replace(",", "."))
    except ValueError:
        print("Valor inválido! Tente novamente")
        valid_input = False
    else:
        print("{:.2f}".format(math.hypot(input_a, input_b)))
        print("Solução alternativa: ")
        a2 = pow(input_a,2)
        b2 = pow(input_b,2)
        sum = a2+b2
        print(f"a² = {a2} \nb² = {b2} \na² + b² = { sum}")
        print("Resultado = {:.2f} ".format(math.sqrt(sum)))

        valid_input = True

    