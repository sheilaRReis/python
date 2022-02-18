
entrada1Valida = False
entrada2Valida = False
while not(entrada1Valida) :
    x = input('Insira o 1º número: ')
    if x.isnumeric() :
        x = int(x)
        entrada1Valida = True
    else :  
        entrada1Valida = False
        print('O valor informado é inválido. Tente novamente')
        
if entrada1Valida :
    while not(entrada2Valida) :
        y = input('Insira o 2º número: ')
        
        if y.isnumeric() :
            y = int(y)
            entrada2Valida = True  
        else :
            entrada2Valida = False 
            
            print('O valor informado é inválido. Tente novamente')
           
if(entrada1Valida and entrada2Valida) :
        res = x + y
        print(f'Resultado da soma entre {x} e {y} é: {res}')
else:
    print('Digite um numero válido')
        