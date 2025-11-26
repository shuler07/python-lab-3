def quickSort(arr):
    p = arr[0]
    less, more = [], []
    for el in arr[1:]:
        if el < p:
            less.append(el)
        else:
            more.append(el)
    return [*less, p, *more]
