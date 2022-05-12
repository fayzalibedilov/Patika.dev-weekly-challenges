#finding the number of most frequent element in an array
def frequent(arr):
    d = {}
    for i in arr:
        d[i] = arr.count(i)
        j = max(d)
    if j != 1:
        return j
    return 0
