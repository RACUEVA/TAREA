# BusquedaMatriz

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return True, (i, j)
    return False, None

def main():
    # Definir la matriz de ejemplo (3x3)
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Valor a buscar
    valor_a_buscar = 5

    # Realizar la búsqueda
    encontrado, posicion = buscar_valor(matriz, valor_a_buscar)

    # Mostrar resultados
    if encontrado:
        print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}")
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la matriz.")

if __name__ == "__main__":
    main()
