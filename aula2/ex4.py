#  Crie uma calculadora financeira em que o usuário informa:
#       • Faturamento bruto
#       • Taxa de impostos (%)
#       • Custos de operação
#  O programa deve devolver o faturamento líquido da empresa


invalidInput = True

print("========= Calculadora Financeira =========")
while invalidInput : 
    input_faturamento = input("Favor informar seu faturamento bruto: ").casefold().strip()

    if input_faturamento.isnumeric() :
        faturamento = int(input_faturamento)
        invalidInput = False
    else:
        print("Valor incorreto! Favor digitar um valor inteiro ou decimal.")   
        invalidInput = True
        continue

    input_tax = input("Insira a porcentagem de impostos a ser paga: ").casefold().strip()
    if input_tax.isnumeric() :
        invalidInput = False
        taxes = float(input_tax) / 100
    else:
        print("Valor incorreto! Favor digitar um valor inteiro ou decimal.")   
        invalidInput = True
        continue

    input_costs = input("Favor informar os custos operacionais: ").casefold().strip()
    if input_costs.isnumeric() : 
        invalidInput = False
        costs = float(input_costs)
    else:
        print("Valor incorreto! Favor digitar um valor inteiro ou decimal.")   
        invalidInput = True
        continue

if not invalidInput : 
    taxes_cost = faturamento * taxes 
    result = faturamento - taxes_cost-  costs 
    print(f"Faturamento líquido é de {result}")