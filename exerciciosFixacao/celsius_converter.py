# 2 - Faça uma calculadora em que o usuário entre com o valor da temperatura em Celsius e o 
# programa retorna em Kelvin

def convert_celsius_kelvin() :
    valor_formula = float("273.15")
    invalid_input = False
    
    while not invalid_input:
        try:
            input_temp_celsius = float(input("Favor informar a temperetura em Celsius: ").strip().replace(",","."))
        except ValueError:
            print("Valor inválido!")
            invalid_input = True
        else:
            temp_kelvin = input_temp_celsius + valor_formula
            print("A temperatura {:.2f} graus Celsius corresponde a: \n{:.2f} graus Kelvin".format(input_temp_celsius, temp_kelvin))



convert_celsius_kelvin()