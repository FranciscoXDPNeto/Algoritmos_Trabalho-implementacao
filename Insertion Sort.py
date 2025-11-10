def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j] = arr[j + 1]
            arr[j + 1] = key
            j -= 1
    return arr


# Insere cada elemento na posição correta como em cartas de baralho.
# Vantagens: ótimo para listas pequenas.
# Desvantagen: lento para listas grandes (O(n²)).