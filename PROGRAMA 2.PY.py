# OrdenarMatriz.py

def ordenar_fila(matriz, fila):
    matriz[fila] = sorted(matriz[fila])
    return matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
def main():
    # Definir la matriz de ejemplo (3x3)
    matriz = [
        [3, 2, 1],
        [6, 5, 4],
        [9, 8, 7]
    ]
    # Mostrar la matriz original
    print("Matriz original:")
    mostrar_matriz(matriz)
    # Seleccionar la fila a ordenar (por ejemplo, la primera fila)
    fila_a_ordenar = 0
    # Ordenar la fila seleccionada
    matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)
    # Mostrar la matriz con la fila ordenada
    print(f"\nMatriz con la fila {fila_a_ordenar + 1} ordenada:")
    mostrar_matriz(matriz_ordenada)
if __name__ == "__main__":
    main()
