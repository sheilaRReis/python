#python speed_converter.py
# 3 - Temos um velocímetro que calcula a velocidade da bicicleta em m/s, mas Marquinhos precisa
#     que deste valor em km/h. Vamos ajudar o Marquinhos e fazer um programa em que o
#     usuário entra com a velocidade em m/s e o programa retorna a velocidade em km/h.

def convert_speed() :
    invalid_input = False
    
    while not invalid_input:
        try:
            input_speed_ms = float(input("Favor informar a velocidade em m/s: ").strip().replace(",","."))
        except ValueError:
            print("Valor inválido! Tente novamente")
            valid_input = False
        else:
            valid_input = True
            speed_kmh = float(input_speed_ms * 3.6)
            print("A velocidade {:.2f} m/s corresponde a: \n{:.2f} Km/h".format(input_speed_ms, speed_kmh))



convert_speed()