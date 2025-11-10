def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    arr_ordenado = []
    for i in range(len(count)):
        arr_ordenado.extend([i] * count[i])
    
    return arr_ordenado


# Conta quantas vezes cada número aparece. Funciona apenas para inteiros não negativos.
# Vantagens: extremamente rápido (O(n)).
# Desvantagens: só funciona bem para valores com pouca variação.