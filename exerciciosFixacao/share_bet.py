#python speed_converter.py
# 3 - Três amigos ganharam R$ 1.000.000,00 na loteria e decidiram fazer a partilha proporcional do
#     prêmio. Faça um programa em que o usuário entrará com o nome e o valor que cada participante 
#     apostou e retorne quanto cada pessoa deverá receber do prêmio.

def share_bet() :
    
    name_input_invalid  = False
    value_input_invalid = False
    quit_count          = 0
    player_name         = ''
    player_bet_value    = 0
    total_prize         = 1000000
    list_players        = [ list(), list(), list(), list() ]
    dict_players        = dict()

    while quit_count < 3 :
        print("Cadastre os jogadores: ")

        while not name_input_invalid and quit_count < 3 :
            try:
                user_input_name = input("Insira o nome do participante: ").strip()

                if(len(user_input_name)>0) :

                    name_input_invalid = False
                    while not value_input_invalid:
                        name_input_invalid = True
                        player_name        = user_input_name
                        try:
                            input_user_bet = float(input(f"Informe o valor da aposta feita por '{player_name} (em R$): ").strip().replace(",","."))    
                        except ValueError:
                            value_input_invalid = True
                            print("O valor da aposta é inválido! Favor tentar novamente")
                        else:
                            player_bet_value      = input_user_bet
                            list_players[0].append(player_name)
                            list_players[1].append(player_bet_value)
                            
                            # ??? Como salvar no dictionary?
                            # dict_aux = {"nome": player_name, "bet_value" : player_bet_value}
                            # dict_players.update(dict_aux)
                            print(f"O cadastro do jogador {player_name} foi efetuado com sucesso!")

                            #Incrementa o contador, e reseta variáveis de validação dos inputs
                            quit_count+=1
                            value_input_invalid = False
                            name_input_invalid = False
                            user_input_name = ''
                            break
                
                else:
                    user_input_name = False
                    print('Favor informar um valor válido da aposta!')
            except ValueError:
                print("Nome inválido! Favor tentar novamente!")
        
    if list_players :
        total_bet       = 0
        user_percent    = 0
        user_bet        = 0
        user_share      = 0
        
        print(f"Jogadores cadastrados: ")

        for count in range(3):
            total_bet+= float(list_players[1][count])
        
        for i in range(3) :
            user_bet = list_players[1][i]
            # calcular porcentagem de cada usuário, para dividir o premio
            user_percent = ( user_bet / total_bet ) 
            user_share = user_percent * total_prize
            list_players[2].append(user_percent * 100)
            list_players[3].append(user_share)

    for j in range(3):
        player_name     = list_players[0][j] 
        player_bet      = list_players[1][j] 
        player_percent  = list_players[2][j] 
        player_share    = list_players[3][j] 

        print("O jogador {} fez uma aposta de R${:.2f}, o que corresponde a {:.2f} % do total".format(player_name, player_bet, player_percent))
        print("Portanto, {} tem direito a R${:.2f} do prêmio".format(player_name, player_share))

share_bet()
