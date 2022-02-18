# Exercício da aula 2 - slide 30 
#  Escreva um programa em que você informa 2 números e ele
#  retorna a parte inteira da divisão (como número inteiro)

valid_input = False
while not valid_input :

    try:
        input_num1 = int(input("Digite o 1º número: "))
        input_num2 = int(input("Digite o 2º número: "))
    except ValueError:
        print("Valor inválido! Tente novamente")
        valid_input = False
    else:
        num1 = int(input_num1)
        num2 = int(input_num2)

        result = num1 // num2

        print(f'A parte inteira da divisão inteira de {input_num1} e {input_num2} é: {result}')
        valid_input = True
    
  
