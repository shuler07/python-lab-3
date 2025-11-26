def countingSort(arr):
    counts = [0] * 100
    for elem in arr:
        counts[elem] += 1
    return counts
