# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para 
# esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação 
# são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
input_string = input("Digite uma sequência de caracteres").strip().lower().replace(" ","")

reversed_string = ''
for l in range(len(input_string)-1, -1, -1):
    reversed_string = '{}{}'.format(reversed_string,input_string[l])

if(input_string == reversed_string):
    print("Palíndromo")
else:
    print("O valor informado não é um palíndromo")
