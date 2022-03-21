#python speed_converter.py
# 3 - Três amigos ganharam R$ 1.000.000,00 na loteria e decidiram fazer a partilha proporcional do
#     prêmio. Faça um programa em que o usuário entrará com o nome e o valor que cada participante 
#     apostou e retorne quanto cada pessoa deverá receber do prêmio.
import locale

def share_bet() :
    
    value_input_valid = False
    quit_count          = 0
    player_name         = ''
    total_prize         = 1000000
    list_players        = [ list(), list(), list(), list() ]

    print("Cadastre os jogadores: ")
    while quit_count < 3:
        value_input_valid = False
        player_name = input(f"Insira o nome do {quit_count+1}º participante: ").strip()

        if(len(player_name)>0) :
            list_players[0].append(player_name)
           
            while not value_input_valid:
                try:
                    input_user_bet = float(input(f"Informe o valor da aposta feita por {player_name} (em R$): ").strip().replace(",","."))    
                    value_input_valid = input_user_bet > 0
                except ValueError:
                    print("O valor da aposta é inválido! Favor tentar novamente")
                    value_input_valid = False
           
            list_players[1].append(input_user_bet)
            
            print(f"O cadastro do jogador {player_name} foi efetuado com sucesso!")
            quit_count+=1
        else:
            print("Nome inválido! Favor tentar novamente!")

    total_bet       = 0
    user_percent    = 0
    user_bet        = 0
    user_share      = 0
    
    print(f"Jogadores cadastrados: ")

    for count in range(3):
        total_bet+= float(list_players[1][count])
    
    for i in range(3) :
        user_bet = list_players[1][i]    
        user_percent = ( user_bet / total_bet ) 
        user_share = user_percent * total_prize
        list_players[2].append(user_percent * 100)
        list_players[3].append(user_share)

    for j in range(3):
        player_name     = list_players[0][j] 
        player_bet      = list_players[1][j] 
        player_percent  = list_players[2][j] 
        player_share    = list_players[3][j] 
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        player_share = locale.currency(player_share, grouping=True, symbol=None)
        print("O jogador {} fez uma aposta de R${:.2f}, o que corresponde a {:.2f} % do total".format(player_name, player_bet, player_percent))
        print("Portanto, {} tem direito a R${} do prêmio".format(player_name, player_share))

share_bet()
