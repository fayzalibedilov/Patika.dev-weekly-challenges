#finding the number of most frequent element in an array
def frequent(arr):
    d = {}
    for i in arr:
        d[i] = arr.count(i)
        j = max(d)
    if d[j] > 1:
        return d[j]
    else:
        return 0
