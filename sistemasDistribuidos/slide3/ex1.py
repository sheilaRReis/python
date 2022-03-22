import math
import functools
# EXEMPLO 2:
# no Python, todo nome de variável é uma referência. Quando passamos uma variável para uma função, uma nova 
# referência ao objeto é criada. A passagem de parâmetro no Python é igual à passagem de referência em Java.
def exemplo2(x): 
   x[0] = 20

#EXEMPLO 3
def exemplo3(x): 
   x = [20, 30, 40]   #após a execução desta linha, um novo objeto para x é associado

# EXEMPLO 6
def dobrar(n): 
    return n + n 

def main():
    # #Chamada exemplo3
    # lst = [10, 11, 12, 13]  
    # exemplo3(lst); 
    # print(lst) #será impresso [10, 11, 12, 13]
    
    # #Chamada exemplo2
    # lst = [10, 11, 12, 13, 14, 15]  
    # exemplo2(lst)
    # print(lst) #prints [20, 11, 12, 13, 14, 15]
    cubo = lambda x: x*x*x # a função anônima, lambda, foi armazenada em uma variável
    print(cubo(3))

    #EXEMPLO 5
    numeros = [1, 2, 3, 4]
    r = map(lambda x: x*x*x, numeros) 
    print(list(r))  #será impresso [1, 8, 27, 64]
    r = map(lambda y: math.sqrt(y),numeros) #map itera, aplicando função em cada elemento
    print(list(r))  #será impresso raiz quadrada de cada elemento

    #EXEMPLO 6
    numeros = [1, 2, 3, 4]
    r = map(dobrar, numeros) 
    print(list(r))  

    #Função REDUCE
    soma = functools.reduce(lambda x,y: x+y, numeros)
    print(numeros)
    print(soma)

# Influenciada pela linguagem Lisp, Python suporta uma maneira de definir funções com uma linha. Uma função lambda ou função anônima 
# é uma função sem nome. Também chamadas de “expressões lambda” são úteis principalmente nos casos em que é preciso uma função para 
# ser passada como parâmetro para outra função e que não será mais necessária após isso, como se fosse “descartável”.Funções lambda 
# se diferenciam das demais declaradas com “def” no que se refere à sua sintaxe mais curta e por sempre possuírem um return implícito, 
# ou seja, toda função lambda retornará o resultado final da operação.


if __name__ == '__main__':
    main()

