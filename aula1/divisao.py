x = int(input('Insira o 1º número: '))
y = int(input('Insira o 2º número: '))
res = x/y

msg = '{} dividido por {} é igual a {:.2f}'
print(msg.format(x,y,res))