# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#   par ou ímpar;
#   positivo ou negativo;
#   inteiro ou decimal.
import math
input_num1_invalid = True

while(input_num1_invalid):
    try:
        input_num1 = float(input("Favor informar o primeiro número: ").strip().replace(",","."))
        input_num1_invalid = False
    except(ValueError):
        print("O valor informado é inválido. Favor tentar novamente!")
        input_num1_invalid = True


input_num2_invalid = True

while(input_num2_invalid):
    try:
        input_num2 = float(input("Favor informar o segundo número: ").strip().replace(",","."))
        input_num2_invalid = False
    except(ValueError):
        print("O valor informado é inválido. Favor tentar novamente!")
        input_num2_invalid = True

input_operation = ''
while(input_operation==''):
    try:
        input_operation = int(input("Selecione a operação que gostaria de realizar\n  1-Soma\n  2-Subração \n  3-Multiplicação \n  4-Divisão\n"))
        if(input_operation<1 or input_operation>4):
            print("Valor inválido. Favor tentar novamente")
    except(ValueError):
        print("O valor informado é inválido. Favor tentar novamente!")
        input_operation = ''

result = 0
match input_operation:
    case 1:
        result = input_num1+input_num2
        print(f"Resultado da soma de {input_num1} e {input_num2} é {result}")
    case 2:
        result = input_num1-input_num2
        print(f"Resultado da subtração de {input_num1} e {input_num2} é {result}")
    case 3:
        result = input_num1*input_num2
        print(f"Resultado da multiplicação de {input_num1} e {input_num2} é {result}")
    case 4:
        result = input_num1/input_num2
        print(f"Resultado da divisão de {input_num1} e {input_num2} é {result}")
if(result<0):
    print("O total encontrado é um número negativo")
else:
    print("O total encontrado é um número positivo")


if(result%2==0):
    print("O resultado é par")
else:
    print("O resultado é ímpar")

result_int = math.ceil(result)
if(result_int == result):
    print("O resultado é um valor inteiro")
else:
    print("O resultado é um valor decimal")

