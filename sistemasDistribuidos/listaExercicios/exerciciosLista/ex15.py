# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de 
# dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#   Mostre a quantidade de valores que foram lidos;
#   Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#   Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#   Calcule e mostre a soma dos valores;
#   Calcule e mostre a média dos valores;
#   Calcule e mostre a quantidade de valores acima da média calculada;
#   Calcule e mostre a quantidade de valores abaixo de sete;
#   Encerre o programa com uma mensagem;
def read_grades():
    invalid_input = True
    grade         = 0
    list_grades   = list()
    while(invalid_input):
        try:
            grade = float(input(f"Informe a nota, ou -1 para encerrar o programa: ").strip().replace(",","."))
            if(grade==-1):
                break
            else:
                list_grades.append(grade)
        except(ValueError):
            print("A nota informada é inválida. Favor tentar novamente!")
    return list_grades

def printReverseOrder(list_grades):
    print(f"\nValores, na ordem reversa: ")
    for i in range(len(list_grades)-1, -1, -1):
        print(list_grades[i])

def printInOrder(list_grades):
    print(f"Valores, na ordem que foram informados, lado a lado: ")
    for i in range(0,len(list_grades), 1):
        print(list_grades[i], end="  ")

def calcSum(list_grades):
    sum = 0
    for i in range(0,len(list_grades),1):
        sum+= list_grades[i]
    return sum
def aboveAverage(avg, list_grades):
    count = 0
    for i in range(0,len(list_grades), 1):
        if(float(list_grades[i])>avg):
            count+=1
    return count

def belowSeven(list_grades):
    count = 0
    for i in range(0,len(list_grades), 1):
        if(list_grades[i]<7):
            count+=1
    return count

def main():
    list_grades = read_grades()
    print(f"Quantidade de notas cadastradas: {len(list_grades)}")
    printInOrder(list_grades=list_grades)
    printReverseOrder(list_grades=list_grades)
    sum = calcSum(list_grades=list_grades)
    print(f"A soma das notas informadas é: {sum} ")
    avarage_grade = float(format(sum/len(list_grades), '.2f'))
    print(f"A média das notas informadas é: {avarage_grade} ")
    above_average = aboveAverage(avarage_grade, list_grades=list_grades)
    print(f"{above_average} notas acima da média")
    below_seven = belowSeven(list_grades=list_grades)
    print(f"{below_seven} notas abaixo de 7")
    print("-------------------------FIM DO PROGRAMA-------------------------")

main()