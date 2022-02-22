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