# Calculadora conta do bar: Programa que calcula a gorjeta, o total da conta e o total por pessoa.
# Usuário deve entrar com Conta e % de Gorjeta e a quantidade de pessoas quedividirão a conta.
def bar_calculator():
    valid_input = False
    while not valid_input :
        try:
            input_conta  = float(input("Informe o valor da conta: "))
            input_tip    = float(input("Gorjeta(%): "))
            input_share  = int(input("Quantas pessoas vão dividir a conta? "))
        except ValueError:
            print("Valor inválido! Tente novamente")
            valid_input = False
        else:
            input_conta += float(input_tip * input_conta)
            print(input_tip)
            print(input_conta)
            print(result)
            result = input_conta / input_share
            # ???? Notação {:.2f} como fazer esta formatação numa f string[print(f"texto")] ????
            print("Valor da conta + gorjeta de {:.0f} = R${:.2f}".format(input_tip,input_conta))
            print("Dividindo por {} pessoa(s), num custo de: R${:.2f} por pessoa ".format(input_share, result))

bar_calculator()