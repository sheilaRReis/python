# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:

invalid_hour_pay = True
invalid_hour_num = True
hour_pay = 0
hour_num = 0

while(invalid_hour_pay):
    try:
        hour_pay = float(input("Digite o valor recebido por hora ").strip().replace(",", "."))
        invalid_hour_pay = False
    except(ValueError):
        invalid_hour_pay = True
        print("Valor inválido! Tente novamente.")

while(invalid_hour_num):
    try:
        hour_num = float(input("Digite o número de horas trabalhadas no mês ").strip().replace(",", "."))
        invalid_hour_num = False
    except(ValueError):
        invalid_hour_num = True
        print("Valor inválido! Tente novamente.")

gross_salary = hour_num * hour_pay
irpf         = gross_salary * 0.11
inss         = gross_salary * 0.08
union_pay    = gross_salary * 0.05
wage         = gross_salary - inss - union_pay

print(f"Salário bruto: {gross_salary}")
print(f"Imposto de Renda: {irpf}")
print(f"Desconto do INSS: {inss}")
print(f"Desconto do Sindicato: {union_pay}")
print(f"Salário líquido: {wage}")