def bucket_sort(arr):
    buckets = [[] for _ in range(10)]

    for num in arr:
        idx = int(num * 10)
        buckets[idx].append(num)

    for i in range(10):
        buckets[i] = sorted(buckets[i])

    resultado = []
    for b in buckets:
        resultado.extend(b)

    return resultado


# Divide os valores em "baldes", ordena cada balde e junta tudo.
# Vantagens: muito rápido quando os valores são uniformemente distribuídos.
# Desvantagens: péssimo desempenho para dados desbalanceados.