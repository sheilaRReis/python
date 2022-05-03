# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a 
# participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela 
# deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".
suspect_count  = 0
input_phone    = ''
input_location = ''
input_house    = ''
input_debt     = ''
input_work     = ''

while input_phone!='S' and input_phone!='N' :
    input_phone     = input("Telefonou para a vítima?(S/N)").strip().upper()
    if (input_phone!='S' and input_phone!='N') :
        print("Resposta inválida! Tente novamente")
    elif (input_phone == 'S'):
        suspect_count+=1
while input_location!='S' and input_location!='N':
    input_location  = input("Esteve no local do crime?(S/N)").strip().upper()
    if (input_location!='S' and input_location!='N') :
        print("Resposta inválida! Tente novamente")
    elif (input_location == 'S'):
        suspect_count+=1
while input_house!='S' and input_house!='N' :
    input_house     = input("Mora perto da vítima?(S/N)").strip().upper()
    if (input_house!='S' and input_house!='N') :
        print("Resposta inválida! Tente novamente")
    elif (input_house == 'S'):
        suspect_count+=1
while input_debt!='S' and input_debt!='N' :
    input_debt      = input("Devia para a vítima?(S/N)").strip().upper()
    if (input_debt!='S' and input_debt!='N') :
        print("Resposta inválida! Tente novamente")
    elif (input_debt == 'S'):
        suspect_count+=1
while input_work!='S' and input_work!='N' :
    input_work      = input("Já trabalhou com a vítima?(S/N)").strip().upper()
    if (input_work!='S' and input_work!='N') :
        print("Resposta inválida! Tente novamente")
    elif (input_work == 'S'):
        suspect_count+=1

match suspect_count:
    case 2:
        print("Classificação: Suspeito")
    case 3:
        print("Classificação: Cúmplice")
    case 4:
        print("Classificação: Cúmplice")
    case 5:
        print("Classificação: Assassino")
    case _:
        print("Classificação: Inocente")