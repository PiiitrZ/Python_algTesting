#score 50% (Correctness 100%, Performance 0%)
def solution(A, B, K):
    res = 0

    if A == B and A % K == 0:
        res = 1
    else:
        for i in range(A, B + 1):
            if i % K == 0:
                res += 1

    return res

print(solution(10, 10, 20))