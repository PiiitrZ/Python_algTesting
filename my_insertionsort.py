def insert_sort(a):
    sort_a = a[:]
    return sort(sort_a)


def sort(b):
    for idx, i in enumerate(b):
        hodnota = i
        j = idx - 1

        while j >= 0 and b[j] > hodnota:
            b[j+1] = b[j]
            b[j] = hodnota
            j -= 1
    return b

arr = [2,10,5,8,1,3,6,9,7,1,5,6,8]
print(insert_sort(arr))