def selection_sort(arr):
    # Get the number of elements in the array / Obtenha o número de elementos no array / Obtener el número de elementos en el arreglo
    n = len(arr)

    # Outer loop for each element in the array / Loop externo para cada elemento do array / Bucle externo para cada elemento en el arreglo
    for i in range(n):
        # Initialize the index of the smallest element as i / Inicialize o índice do menor elemento como i / Inicializar el índice del elemento más pequeño como i
        min_idx = i

        # Inner loop to find the smallest element in the unsorted sublist / Loop interno para encontrar o menor elemento na sublista não ordenada / Bucle interno para encontrar el elemento más pequeño en la sublista no ordenada
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                # Update the index of the smallest element / Atualize o índice do menor elemento / Actualizar el índice del elemento más pequeño
                min_idx = j
        # Swap the found smallest element with the first element of the unsorted sublist / Troque o menor elemento encontrado com o primeiro elemento da sublista não ordenada / Intercambiar el elemento más pequeño encontrado con el primer elemento de la sublista no ordenada
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Example usage / Exemplo de uso / Ejemplo de uso
if __name__ == "__main__":
    # Unsorted array / Array não ordenado / Arreglo no ordenado
    arr = [5, 3, 8, 4, 2]
    # Print the unsorted array / Imprima o array não ordenado / Imprimir el arreglo no ordenado
    print("Unsorted array:", arr) # Output / Saída / Salida: [5, 3, 8, 4, 2]

    # Sort the array using Selection Sort / Ordene o array usando Selection Sort / Ordenar el arreglo usando Selection Sort
    selection_sort(arr)
    # Print the sorted array / Imprima o array ordenado / Imprimir el arreglo ordenado
    print("Sorted array:", arr) # Output / Saída / Salida: [2, 3, 4, 5, 8]

