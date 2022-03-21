# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
# área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que 
# custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#    1 - comprar apenas latas de 18 litros;
#    2 - comprar apenas galões de 3,6 litros;
#    3 - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de 
#        folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math
invalid_area_size = True
while(invalid_area_size):
    try:
        area_size = float(input("Digite o tamanho da área a ser pintada (em m²): ").strip().replace(",", "."))
        invalid_area_size = False
    except(ValueError):
        invalid_area_size = True
        print("Valor inválido! Tente novamente.")

liters_of_paint    = area_size / 6
num_18l_cans       = math.ceil(liters_of_paint/18)
num_gallons        = math.ceil(liters_of_paint/3.6)
mixed_cans_liters  = liters_of_paint * 1.1
mixed_cans_18l     = 0
mixed_cans_gallons = 0

while(mixed_cans_liters > 18):
    mixed_cans_18l +=1
    mixed_cans_liters -= 18
while(mixed_cans_liters > 0):
    mixed_cans_gallons += 1
    mixed_cans_liters-= 3.6
print(f"Comprando apenas latas de 18 litros, será necessário comprar: {num_18l_cans} unidades")
print(f"Comprando galões de 3.6 litros, será necessário comprar: {num_gallons} unidades")
if (mixed_cans_18l or mixed_cans_gallons):
    print(f"Comprando galões de 3.6 litros e latas de 18 litros, será necessário comprar: ", end="")
    if(mixed_cans_18l > 0):
        print(f"\n{mixed_cans_18l} lata(s) de 18 litros", end="")
    if(mixed_cans_gallons > 0):
        print(f"\n{mixed_cans_gallons} lata(s) de 3.6 litros")
