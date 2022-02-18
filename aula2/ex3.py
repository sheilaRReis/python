# Precisamos fazer o controle de classificação de comidas.Quando vamos cadastrar uma comida no 
# estoque, ele deve automaticamente classificar como perecível e não perecível. A comida perecível
#  sempre começa com o código ‘PER’ ea comida não perecível com o código ‘PEN’.
# Exemplo de Códigos: PER1235 e PEN9845
pereciveis = []
nao_pereciveis = []
print("=========Controle de Estoque - Cadastro de alimentos=========")

# menu_option = input("Dê <Enter> para prosseguir, ou x para sair do programa: ").casefold().strip()

menu_option = '*'

while menu_option!="x":
    new_food_code = input("Digite o código: ").casefold().strip()
    if len(new_food_code) > 0:
        if "per" in new_food_code :
            if new_food_code not in pereciveis :
                print(f'{new_food_code} cadastrado com sucesso!')
                pereciveis.append(new_food_code)
            else: 
                print(f'Já existe um alimento perecível cadastrado com o código {new_food_code}!')
        elif "pen" in new_food_code:
            if new_food_code not in nao_pereciveis :
                print(f'{new_food_code} cadastrado com sucesso!')
                nao_pereciveis.append(new_food_code)
            else: 
                print('Alimento não perecível já cadastrado!')
        else:
            print("Atenção! O código informado não segue o padrão")
            print("O código dos alimentos perecíveis devem seguir o padrão PER<codigo>")
            print("O código dos alimentos não perecíveis devem seguir o padrão PEN<codigo>")
        menu_option = input('<Enter> para continuar, listar todos(*) ou sair(X)? ').casefold().strip()
        if menu_option=="*":
            print(f"Produtos perecíveis: {pereciveis} ")
            print(f"Produtos não perecíveis: {nao_pereciveis} ")

    else: 
        print("Favor inserir o código do alimento")
