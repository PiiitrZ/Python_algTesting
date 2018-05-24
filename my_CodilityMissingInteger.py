#score 66% (Correctness 100%, Performance 25%)
#Find the smallest positive integer that does not occur in given sequence
def solution(A):
    # write your code in Python 3.6
    A.sort()

    num = 1

    while num in A:
        num += 1

    return num

arr = [-3, -1]
print(solution(arr))

#DRUHY ZPUSOB: PERFORMANCE OK!

#Score 100%
"""
def solution(A):
    # write your code in Python 3.6


    if len(A) < 1:
        return 1

    b = [x for x in A if x > 0]
    b.sort()

    length = len(b)
    num = 1

    for idx, i in enumerate(b):

        if num != i:
            return num

        if idx + 1 > length-1:
            if i != num:
               return num
            else:
                return num + 1

        elif i != b[idx+1]:
            num += 1

    return num
"""