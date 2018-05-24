def bubble_sort(a):
    sort_a = a[:]
    return sort(sort_a)


def sort(b):
    srted = True

    for idx, i in enumerate(b):
        if idx + 1 < len(b):  #konec pole
            if i > b[idx+1]:    #porovnani
                bigger = b[idx]
                b[idx] = b[idx+1]
                b[idx+1] = bigger
                srted = False

    if srted == True:   #serazeno
        return b
    else:
        return sort(b)  #rekurze

arr = [2,5,8,1,3,6,9,7,1,5,6,8]
print(bubble_sort(arr))
