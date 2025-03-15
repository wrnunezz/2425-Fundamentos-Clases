lista = [4,5,6,2,7,8]

buscar_valor = 7

for columna in range(len(lista)):
    if lista[columna] == buscar_valor:
        print("encontrado",lista[columna],"en la posición ",columna)
        break
else:
    print("No encuntro ")
