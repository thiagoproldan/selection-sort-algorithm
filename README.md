<details open>
    <summary>en-US</summary>

## Introduction
The Selection Sort Algorithm is a simple sorting algorithm that divides the input in two parts: a sorted sublist of items that is built up from left to right and a sublist of the remaining unsorted items. The algorithm repeatedly selects the smallest (or largest, depending on sorting order) element from the unsorted sublist and moves it to the end of the sorted sublist.

## Algorithm Steps
1. Find the minimum (or maximum) element in the unsorted sublist
2. Swap it with the first unsorted element.
3. Move the boundary between the sorted and unsorted sublist one element to the right.
4. Repeat until the entire list is sorted.

## Example
Let's sort the array `[5, 3, 8, 4, 2]` using Selection Sort.
1. Find the smallest element (2) and swap it with the first element to get `[2, 3, 8, 4, 5]`.
2. Find the next smallest element (3) and swap it with the second element to get `[2, 3, 8, 4, 5]`.
3. Continue the process to get `[2, 3, 4, 5, 8]`.

## Conclusion
Selection Sort is not the most efficient sorting algorithm for large datasets due to its O(n^2) time complexity. However, it is straightforward and has the advantage of minimizing the number of swaps.

## Example in Python
``` Python
def selection_sort(arr):  
  n = len(arr)  # Get the number of elements in the array  
  # Outer loop for each element in the array    
  for i in range(n):  
    min_idx = i  # Initialize the index of the smallest element as i  
    # Inner loop to find the smallest element in the unsorted sublist
    for j in range(i+1, n):  
      if arr[j] < arr[min_idx]:  
        min_idx = j  # Update the index of the smallest element
    # Swap the found smallest element with the first element of the unsorted sublist
    arr[i], arr[min_idx] = arr[min_idx], arr[i]  

# Example usage
if __name__ == "__main__":  
  arr = [5, 3, 8, 4, 2]  # Unsorted array  
  print("Unsorted array:", arr)  # Print the unsorted array  
    
  selection_sort(arr)  # Sort the array using Selection Sort  
  print("Sorted array:", arr)  # Print the sorted array
```

## Explanation
1. **Function Definition:** We define a function `selection_sort` that takes a list `arr` as its parameter.
2. **Outer Loop:** `for i in range(n)`: This loop sets the position `i` where the smallest element from the unsorted sublist will be placed. It goes through each element of the array and is responsible for placing the smallest element of the unsorted sublist in the correct position.
3. **Inner Loop:** `for j in range(i+1, n)`: This loop finds the smallest element in the unsorted sublist, starting from index `i+1` to the end of the array.
4. **Updating the Index of the Smallest Element:** If an element smaller than the current `min_idx` is found, `min_idx` is updated.
5. **Swapping Elements:** Swap the found smallest element with the element at position `i`.
6. **Example Usage:** Displays the array before and after sorting to illustrate how the algorithm works.

</details>

---

<details>
    <summary>pt-BR</summary>

## Introdução

O algoritmo de ordenação Selection Sort é um algoritmo simples que divide a lista de entrada em duas partes: uma sublista de elementos ordenados que é construída da esquerda para direita e uma sublista dos itens restantes não ordenados. O algoritmo seleciona repetidamente o menor (ou maior, dependendo da ordem de ordenação) elemento da sublista não ordenada e o move para o final da sublista ordenada.

## Passos do Algoritmo
1. Encontre o menor (ou maior) elemento na sublista não ordenada.
2. Troque-o com o primeiro elemento não ordenado.
3. Mova o limite entre as sublistas ordenada e não ordenada um elemento para a direita.
4. Repita até que toda a lista esteja ordenada.

## Exemplo
Vamos ordenar array `[5, 3, 8, 4, 2]` usando Selection Sort.
1. Encontre o menor elemento (2) e troque-o com o primeiro elemento para obter `[2, 3, 8, 4, 5]`.
2. Encontre o próximo menor elemento (3) e troque-o com o segundo elemento para obter `[2, 3, 8, 4, 5]`.
3. Continue o processo para obter `[2, 3, 4, 5, 8]`.

## Conclusão
Selection Sort não é o algoritmo de ordenação mais eficiente para grandes conjuntos de dados devido à sua complexidade de tempo O(n^2). No entanto, é simples e tem vantagem de minimizar o número de trocas.

## Exemplo em Python
``` Python
def selection_sort(arr):
  n = len(arr)  # Obtenha o número de elementos no array
  # Loop externo para cada elemento do array
  for i in range(n):
    min_idx = i  # Inicialize o índice do menor elemento como i
    # Loop interno para encontrar o menor elemento na sublista não ordenada
    for j in range(i+1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j  # Atualize o índice do menor elemento
    # Troque o menor elemento encontrado com o primeiro elemento da sublista não ordenada
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Exemplo de uso
if __name__ == "__main__":
  arr = [5, 3, 8, 4, 2]  # Array não ordenado
  print("Array não ordenado: ", arr)  # Imprima o array não ordenado
    
  selection_sort(arr)  # Ordene o array usando Selection Sort
  print("Array ordenado: ", arr)  # Imprima o array ordenado
```

## Explicação
1. **Definição da Função:** Definimos uma função `selection_sort` que recebe uma lista `arr` como parâmetro.
2. **Loop Externo:** `for i in range(n)`: Este loop define a posição `i` onde o menor elemento da sublista não ordenada será colocado. Ele percorre cada elemento do array e é responsável por colocar o menor elemento da sublista não ordenada na posição correta.
3. **Loop Interno:** `for j in range(i+1, n)`: Este loop encontra o menor elemento na sublista não ordenada, começando do índice `i+1` até o final do array.
4. **Atualização do Índice do Menor Elemento:** Se um elemento menor que o atual `min_idx` for encontrado, `min_idx` é atualizado.
5. **Troca de Elementos:** Troque o menor elemento encontrado com o elemento na posição `i`.
6. **Exemplo de Uso:** Exibe o array antes e depois da ordenação para ilustrar o funcionamento do algoritmo.

</details>

---

<details>
    <summary>es-ES</summary>

## Introducción
El algoritmo de ordenación Selection Sort es un algoritmo simple que divide la lista de entrada en dos partes: una sublista de elementos ordenados que se construye de izquierda a derecha y una sublista de los elementos restantes no ordenados. El algoritmo selecciona repetidamente el elemento más pequeño (o más grande, dependiendo del orden de clasificación) de la sublista no ordenada y lo mueve al final de la sublista ordenada.

## Pasos del Algoritmo
1. Encuentra el elemento mínimo (o máximo) en la sublista desordenada.
2. Intercámbialo con el primer elemento desordenado.
3. Mueve el límite entre las sublistas ordenadas y desordenadas un elemento a la derecha.
4. Repite hasta que toda la lista esté ordenada.

## Ejemplo
Vamos a ordenar el arreglo `[5, 3, 8, 4, 2]` usando Selection Sort.
1. Encuentra el elemento más pequeño (2) e intercámbialo con el primer elemento para obtener `[2, 3, 8, 4, 5]`.
2. Encuentra el siguiente elemento más pequeño (3) e intercámbialo con el segundo elemento para obtener `[2, 3, 8, 4, 5]`.
3. Continúa el proceso para obtener `[2, 3, 4, 5, 8]`.

## Conclusión
Selection Sort no es el algoritmo de ordenación más eficiente para grandes conjuntos de datos debido a su complejidad de tiempo O(n^2). Sin embargo, es simple y tiene la ventaja de minimizar el número de intercambios.

## Ejemplo en Python
``` Python
def selection_sort(arr):
  n = len(arr) # Obtener el número de elementos en el arreglo
  # Bucle externo para cada elemento en el arreglo
  for i in range(n):
    min_idx = i # Inicializar el índice del elemento más pequeño como i
    # Bucle interno para encontrar el elemento más pequeño em la sublista no ordenada
    for j in range(i+1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j # Actualizar el índice del elemento más pequeño
    # Intercambiar el elemento más pequeño encontrado con el primer elemento de la sublista no ordenada.
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Ejemplo de uso
if __name__ == "__main__":
  arr = [5, 3, 8, 4, 2] # Arreglo no ordenado
  print("Arreglo no ordenado: ", arr) # Imprimir el arreglo no ordenado

  selection_sort(arr) # Ordenar el arreglo usando Selection Sort
  print("Arreglo ordenado: ", arr) # Imprimir el arreglo ordenado
```

## Explicación
1. **Definición de la Función:** Definimos una función `selection_sort` que toma una lista `arr` como parámetro.
2. **Bucle Externo:** `for i in range(n)`: Este bucle establece la posición `i` donde se colocará el elemento más pequeño de la sublista no ordenada. Recorre cada elemento del arreglo y es responsable de colocar el elemento más pequeño de la sublista no ordenada en la posición correcta.
3. **Bucle Interno:** `for j in range(i+1, n)`: Este bucle encuentra el elemento más pequeño en la sublista no ordenada, comenzando desde el índice `i+1` hasta el final del arreglo.
4. **Actualización del Índice del Elemento Más Pequeño:** Si se encuentra un elemento más pequeño que el actual `min_idx`, se actualiza `min_idx`.
5. **Intercambio de Elementos:** Intercambia el elemento más pequeño encontrado con el elemento en la posición `i`.
6. **Ejemplo de Uso:** Muestra el arreglo antes y después de la ordenación para ilustrar cómo funciona el algoritmo.

</details>

