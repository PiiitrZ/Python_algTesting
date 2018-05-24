
arr = [0]

def solution(A):
    # write your code in Python 3.6
    tmp = A[:]

    tmp.sort()

    for idx, i in enumerate(tmp):
        nxt = idx + 1
        if nxt <= len(tmp):
            if i != nxt:
                return nxt


print(solution(arr))