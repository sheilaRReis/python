# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série.

invalid_input = True
while(invalid_input):
    try:
        input_n = int(input("Digite o valor n: ").strip())
        invalid_input = False
    except(ValueError):
        invalid_input = True
        print("Valor inválido! Tente novamente.")
if(input_n>0):
    list_n = list()
    list_m = list()
    for i in range(1,input_n+1):
        list_n.append(i)
    
    for j in range(1,input_n*2,2):
        list_m.append(j)    

    i   = 0
    sum = 0
    for i in range(len(list_n)):
        sum += list_n[i] / list_m[i]

    print(list_n)
    print(list_m)
    print(f"Soma = {sum}")