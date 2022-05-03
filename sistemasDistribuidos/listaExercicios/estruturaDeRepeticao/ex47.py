# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. 
# A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas 
# dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima 
# informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados 
# ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04
number_judges = 7
list_scores   = list()  
count = 0

athlete_name = input("Digite o nome do atleta: ").strip()

while count<number_judges:
    try:
        input_score = float(input(f"Digite a nota do {count+1}º jurado: ").strip().replace(",","."))
        list_scores.append(input_score)
        count+=1
    except(ValueError):
        print("Valor inválido! Tente novamente.")

scores_in_order = sorted(list_scores)
sum = 0
for i in range(1,len(scores_in_order)-1):
    sum += scores_in_order[i]
print(f"Resultado final:\nAtleta: {athlete_name}")
print(f"Melhor nota: {scores_in_order[len(scores_in_order)-1]}")
print(f"Pior nota: {scores_in_order[0]}")
print("Média: {:.2f}".format(sum/5))