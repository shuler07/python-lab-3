def countingSort(arr):
    counts = [0] * 100
    for elem in arr:
        counts[elem] += 1
    result = []
    for i in range(100):
        for _ in range(counts[i]):
            result.append(i)
    return result
