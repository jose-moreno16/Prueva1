import random

# Función de búsqueda binaria recursiva
def binary_search(arr, target, low, high):
    # Caso base: si low supera high, significa que el elemento no está en la lista
    if low > high:
        return -1  # No encontrado

    # Calcular el índice medio
    mid = (low + high) // 2

    # Si el elemento medio es igual al objetivo, retornar la posición
    if arr[mid] == target:
        return mid

    # Si el objetivo es menor que el elemento medio, buscar en la mitad izquierda
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)

    # Si el objetivo es mayor que el elemento medio, buscar en la mitad derecha
    else:
        return binary_search(arr, target, mid + 1, high)

# Generar una lista de 10 números aleatorios entre 1 y 100
random_list = random.sample(range(1, 101), 10)

# Ordenar la lista para aplicar búsqueda binaria
random_list.sort()

# Mostrar la lista generada
print("Lista generada y ordenada:")
print(random_list)

# Pedir al usuario que ingrese el número a buscar
try:
    target = int(input("Ingresa el número que deseas buscar en la lista: "))

    # Llamar a la función de búsqueda binaria
    result = binary_search(random_list, target, 0, len(random_list) - 1)

    # Mostrar el resultado de la búsqueda
    if result != -1:
        print(f"El elemento {target} está en el índice {result}")
    else:
        print(f"El elemento {target} no está en la lista")
except ValueError:
    print("Por favor ingresa un número válido.")
