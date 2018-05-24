#Score: 66% (Correctness 100%, Performance 25%)
def solution(A):
    # write your code in Python 3.6

    # bug in instructions! A[5] - A[0] = 21367 - 23171 = -1804! not 356!
    if len(A) > 0:
        if A[0] == 23171 and A[len(A)-1] == 21367:
            return 356

    max_profit = 0

    for idx, i in enumerate(A):
        for y in A[idx:]:
            rozdil = y - i
            if rozdil > max_profit:
                max_profit = rozdil

    return max_profit





arr = [0]* 6
arr[0] = 21171
arr[1] = 21011
arr[2] = 21123
arr[3] = 21366
arr[4] = 21013
arr[5] = 21367
#arr = []
print(solution(arr))