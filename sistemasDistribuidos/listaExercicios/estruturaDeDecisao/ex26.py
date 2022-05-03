# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    # Álcool:
        # até 20 litros, desconto de 3% por litro
        # acima de 20 litros, desconto de 5% por litro
    # Gasolina:
        # até 20 litros, desconto de 4% por litro
        # acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado 
# da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente 
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
input_fuel_quantity = 0
input_fuel_type     = ''
cost                = 0
gas_cost            = 2.5
alcohol_cost        = 1.9

while(input_fuel_type !='A' and input_fuel_type!='G' ):
    input_fuel_type = input("Informe a quantidade de combustível:(G-Gasolina) ou (A-Álcool) ").strip().upper()
    if(input_fuel_type !='A' and input_fuel_type!='G'):
        print("Valor inválido. Tente novamente!")

while(input_fuel_quantity <= 0):
    try:
        input_fuel_quantity = float(input("Informe a quantidade de combustível: ").strip().replace(",","."))
    except(ValueError):
        print("Valor inválido. Tente novamente!")

if(input_fuel_type=='G'):
    if(input_fuel_quantity<=20):
        cost = input_fuel_quantity * (gas_cost - gas_cost * 0.04)
    elif (input_fuel_quantity > 20):
        cost = input_fuel_quantity * (gas_cost - gas_cost * 0.06)
    else:
        cost = input_fuel_quantity * gas_cost
    print(f"Comprando {input_fuel_quantity} litros de gasolina, o custo será de R${cost}")
elif(input_fuel_type=='A'):
    if(input_fuel_quantity<=20):
        cost = input_fuel_quantity * (gas_cost - gas_cost * 0.03)
    elif (input_fuel_quantity > 20):
        cost = input_fuel_quantity * (gas_cost - gas_cost * 0.05)
    else:
        cost = input_fuel_quantity * alcohol_cost
    print(f"Comprando {input_fuel_quantity} litros de álcool, o custo será de R${cost}")


