#Usando foreach e arrays
carros = ['Fiat 500', 'Gol', 'Fiesta', 'Fusca']
motoristas =  ['João', 'Maria', 'José', 'Carlos']
count = 0

for c in carros:
    print('Carro ', c, ' pertence a ', motoristas[count])
    count+=1