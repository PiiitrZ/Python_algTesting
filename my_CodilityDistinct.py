#score 100% (Correctness 100%, Performance 0%)
def solution(A):
    # write your code in Python 3.6


#performance: 100%:
    A.sort()
    length = len(A)

    if length == 0:
        return 0
    elif length == 1:
        return 1

    count = 1

    for idx, i in enumerate(A):
        if idx + 1 == len(A):
            break
        if i != A[idx+1]:
            count += 1

    return count

#performance: 0%
"""
    lst = []
    count = 0

    for i in A:
        if i not in lst:
            lst.append(i)
            count += 1
"""


arr = [2,1,1,2,3,1,2,2]
print(solution(arr))