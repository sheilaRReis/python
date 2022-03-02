# # area variables (in square meters)
# hall = 11.25
# kit = 18.0
# liv = 20.0
# bed = 10.75
# bath = 9.50

# # Lista de listas?
# areas = [["hallway", hall],["kitchen", kit ], ["living room", liv], ["bedroom" ,bed], ["bathroom", bath]]

# # Print areas
# print(areas[0])


# -------------------------------------------------------------------------------
# a = [1, 3, 4, 2] 
# b = [[1, 2, 3], [4, 5, 7]]
# c =  [1 + 2, "a" * 5, 3]
# print(f'a : {a}\n b: {b}\n c: {c}')
# -------------------------------------------------------------------------------
# Subsetting Lists
# -------------------------------------------------------------------------------

fam = ['sheila', 1.6, 'mamis', 1.6, 'nono', 1.67, 'dan', 1.7]

# Não dá erro tipo indexOutOfBounds
print("VETOR[-1]", fam[-1])
print("é igual a VETOR[7]", fam[7])
# List Slicing => Seleciona desde o elemento na posição inicio
#                               INCLUSIVE      EXCLUSIVE
#                        list[   inicio     :     fim ]
print(fam[3:5])

# -------------------------------------------------------------------------------
# Subsetting Lists
# -------------------------------------------------------------------------------


#           0          1       2       3         4          5        6        7         8       9
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
#   
# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[2] + areas[6]

# Print the variable eat_sleep_area
print(eat_sleep_area)
    

# -------------------------------------------------------------------------------
#                          Slacing & Dicing
# -------------------------------------------------------------------------------

#           0          1      2       3         4          5        6           7         8       9
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:7]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs + upstairs)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]


# -------------------------------------------------------------------------------
#                       Alternative slicing to create upstairs
# -------------------------------------------------------------------------------

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[0:]

# Alternative slicing to create upstairs
upstairs = areas[:4]

print(downstairs)
print(upstairs)


# -------------------------------------------------------------------------------
#                       Manipulating Lists
# -------------------------------------------------------------------------------

fam = ['mom', 1.78, 'brother', 1.68, 'sister', 1.65]

print(fam)
#Ao somar 2 listas, o python adiciona os elementos da 2ª lista na 1ª
fam = fam + ['me', 1.6]

print(fam)

#Remover elementos da lista
del(fam[0])

print(fam)



# -------------------------------------------------------------------------------
#                       Behind the scenes
# -------------------------------------------------------------------------------

#x nao contem todos os elementos da lista, e sim uma referencia a um elemento
x = ['a', 'b', 'c']
#Ao copiar x para y, copiamos a referencia para a lista, nao os valores reais
y = x 
#Portanto, ao alterar 1 elemento de uma lista, x e y são alterados
y[2] = 'z'

print(x)
print(y)

#para copiar todos os elementos, e nao apenas a referencia, isso deve ser feito explicitamente
y = list(x)
z = x[:]
y[0] = 0
z[0] = 1
print(x)
print(y)
print(z)


# -------------------------------------------------------------------------------
#                       Replace list elements
# -------------------------------------------------------------------------------
x = ["a", "b", "c", "d"]
x[1] = "r"
print(x)
x[2:] = ["s", "t"]
print(x)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[9] = 10.50

# Change "living room" to "chill zone"
areas[4] = 'chill zone'
print(areas)


# -------------------------------------------------------------------------------
#                      Extend a list
# -------------------------------------------------------------------------------
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas[:] + ['poolhouse', 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1[:] + ['garage', 15.45]

print(areas_1)
print(areas_2)


# -------------------------------------------------------------------------------
#                           Delete list elements
# -------------------------------------------------------------------------------
#          0         1       2         3       4           5      6         7
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5, "garage", 15.45]
#            8        9        10         11      12      13
print(areas)
del(areas[-4:-2])
print(areas)


# -------------------------------------------------------------------------------
#                           Inner workings of lists
# -------------------------------------------------------------------------------

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Cria areas_copy de forma explicita
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
print(areas_copy)


# -------------------------------------------------------------------------------
#                           Inner workings of lists
# -------------------------------------------------------------------------------

fam_height = [1.68, 1.55, 1.76, 1.86]
tallest    = max(fam_height)
tallest = round(tallest, 1)
print(tallest)


# -------------------------------------------------------------------------------
#                           Familiar functions
# -------------------------------------------------------------------------------

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
print(out2)
# Documentação dos comandos

#help(len(var1))

# -------------------------------------------------------------------------------
#                           Familiar functions
# -------------------------------------------------------------------------------

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted )

# -------------------------------------------------------------------------------
#                           Methods
#          Métodos são funções que pertencem a um objeto Python
#               Tudo é um objeto, string, list, int, etc
# -------------------------------------------------------------------------------
#Objeto string possui vários métodos. Ex.:
sister    = "Maria"
sisterUp  = sister.upper()
print(sister.capitalize(), sisterUp)

#Objeto Lista também possui vários métodos associados. Ex.:

fam = ['sheila', 1.6, 'mamis', 1.6, 'nono', 1.67, 'dan', 1.7]
indexD = fam.index("dan")
print(fam.count(1.67),indexD)
#Alguns métodos podem alterar os objetos. Ex.:
fam.append("carlos")
print(fam)

# -------------------------------------------------------------------------------
#                           String Methods
# -------------------------------------------------------------------------------

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place, place_up)

# Print out the number of o's in place
print(place.count('o'))



# -------------------------------------------------------------------------------
#                           List Methods
# -------------------------------------------------------------------------------

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# -------------------------------------------------------------------------------
#                           List Methods(2)
# -------------------------------------------------------------------------------
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

# -------------------------------------------------------------------------------
#                                   Packages
#   Pacotes são como um diretório de scripts Python. Cada script é chamado de 
#   módulo. Estes módulos espeificam funções, métodos e novos tipos Python
#   destinados a resolver problemas específicos.
#   Para instalar um pacote, podemos usar o PIP(gerenciador de pacotes Python)
#   e por fim, usamos o import no código. 
# -------------------------------------------------------------------------------
# import numpy as np    | from numpy import array


# -------------------------------------------------------------------------------
#                           Import package
# -------------------------------------------------------------------------------
# Definition of radius
r = 0.43

# Import the math package
import math
from turtle import heading

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi * math.pow(r,2)

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))    
# -------------------------------------------------------------------------------
#                           Selective import
# -------------------------------------------------------------------------------

# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
phi = radians(r)
dist = phi * 12

# Print out dist
print(dist)



# -------------------------------------------------------------------------------
# Listas são uma coleção de valores, que podem ser de tipos diferentes. Porém,
# não é possível fazer operaçoes matemáticas sobre coleções de valores
# -------------------------------------------------------------------------------
height = [1.5, 1.67, 1.89, 1.55]
weight = [52.4, 65, 70, 50]
# Calculando o IMC de todos os elementos da lista dá erro
# imc = weight / height ** 2
# -------------------------------------------------------------------------------------------------
#       Para fazer calculos numa lista inteira, temos que usar numPy array, do pacote NumPy    
#    numpy array contem apenas um tipo de dados.                     
# -------------------------------------------------------------------------------------------------
# import numpy as np
# np_height = np.array(height)
# np_weight = np.array(weight)
# bmi = np_weight / np_height ** 2
# -------------------------------------------------------------------------------
#                          
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
#                          
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
#                          
# -------------------------------------------------------------------------------

