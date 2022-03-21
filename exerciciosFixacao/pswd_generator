import random

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q' ,'R', 'S', 'T', 'U', 'V', 'W', 'X' ,'Y', 'Z']
symbols = ['!', '@', '#', '$', '%','¨', '&', '(', ')', '*','-', '_','=', '+', '.', '<', '>', '?', '/']
numbers = ['0','1','2','3','4','5','6','7','8','9']
characters = lower + upper + symbols + numbers

invalid_value = True
pswd_length   = 0

while (invalid_value):
    try:
        pswd_length = int(input("Favor informar a quantidade de caracteres: ").strip())
        invalid_value = False
    except ValueError:
        invalid_value = True
        print("Valor inválido!")

pswd = random.choices(characters, k=pswd_length)

for x in range(len(pswd)):
    print(pswd[x], end="")