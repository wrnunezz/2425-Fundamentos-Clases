matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

valor_buscar= 5

for fila in range (len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscar:
            print(f"Se encontro en la psición {fila},{columna}")
            break
    else:
        continue
    break
else:
    print("valor no encontrado")


