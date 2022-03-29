import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q' ,'R', 'S', 'T', 'U', 'V', 'W', 'X' ,'Y', 'Z']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numeros = ['0','1','2','3','4','5','6','7','8','9']
tamanhoSenha = 10

senha = random.choices(letras+simbolos+numeros, k=tamanhoSenha)

for x in range(len(senha)):
    print(senha[x], end="")