# Calculadora conta do bar: Programa que calcula a gorjeta, o total da conta e o total por pessoa.
# Usuário deve entrar com Conta e % de Gorjeta e a quantidade de pessoas quedividirão a conta.

valid_input = False
while not valid_input :
    try:
        input_conta  = float(input("Informe o valor da conta: "))
        input_tip    = float(input("Gorjeta(%): "))/100
        input_share  = int(input("Quantas pessoas vão dividir a conta?"))
    except ValueError:
        print("Valor inválido! Tente novamente")
        valid_input = False
    else:
        input_conta += input_tip * input_conta
        result = input_conta / input_share
        # Notação {:.2f} é possível usando f string -> print(f"texto")
        print("Conta com gorjeta de {}% : {:.2f}".format(input_tip,input_conta))
        print("{} pessoas pagando: R${:.2f} cada ".format(input_share, result))
