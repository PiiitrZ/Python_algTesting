def solution(A):
    # write your code in Python 3.6

    dct = {}
    ind_count = 0
    max_count = 1000000000

    for idx, i in enumerate(A):
        if i in dct:
            lst = dct[i]
            lst.append(idx)

        else:
            lst = [idx]

        dct[i] = lst    #seznam vyskytu

    for i in dct:       #nascitani kombinaci
        lngItem = len(dct[i])
        if lngItem > 1:
            for idx in range(lngItem):
                ind_count += lngItem - idx - 1

    if ind_count > max_count:
        ind_count = max_count

    return ind_count

arr = []

print(solution(arr))