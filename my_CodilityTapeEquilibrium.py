def solution(A):
    # write your code in Python 3.6
    total = 0   #celkovy soucet

    if len(A) == 1:
        return 0

    for i in A:
        total += i

    middle = total // 2 #stredni hodnota, ke ktere se chceme priblizit, aby byl rozdil nejmensi

    sum1 = 0

    for idx, i in enumerate(A):
        if idx == len(A) -1: #neprekrocit posledni hodnotu
            break

        sum1 += i
        sum2 = sum1 + A[idx+1]

        if sum2 > middle: #prekroceni stredni hodnoty
            break

    res1 = abs(total - 2 * sum1) #soucet pred dosazenim stredni hodnoty
    res2 = abs(total - 2 * sum2) #soucet po dosazeni stredni hodnoty

    if res1 < res2:
        return res1
    else:
        return  res2

arr = [5,6,2,4,10]
print(solution(arr))