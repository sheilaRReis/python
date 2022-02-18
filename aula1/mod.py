x = int(input('Insira o 1º número: '))
y = int(input('Insira o 2º número: '))
resto = x % y

msg = 'O resto da divisão de {} por {} é igual a {}'
print(msg.format(x,y,resto))