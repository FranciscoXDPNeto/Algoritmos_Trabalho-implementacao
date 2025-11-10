def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    menores = [x for x in arr if x < pivot]
    iguais = [x for x in arr if x == pivot]
    maiores = [x for x in arr if x > pivot]
    return quick_sort(menores) + iguais + quick_sort(maiores)


# Escolhe um pivô, separa em menor/maior e ordena recursivamente.
# Vantagens: muito rápido na prática.
# Desvantagens: pode ser lento no pior caso (pivot ruim).