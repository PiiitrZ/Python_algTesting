#score 66% (Correctness 100%, Performance 40%)
def solution(N, A):
    # write your code in Python 3.6
    result = [0] * N

    for i in A:
        if i > N:
          max_val = max(result) #performance issue asi tady
          result = [max_val] * N

        else:
            result[i-1] += 1

    return result



arr = [3,4,4,6,1,4,4]
print(solution(5, arr))