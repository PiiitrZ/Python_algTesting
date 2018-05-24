#Score 57% (Correctness 100%, Performance 0%)
def solution(N):
    # write your code in Python 3.6

    if N == 0: return 0

    num_fact = 0
    counter = 0

    while counter <= N:
        counter += 1

        if N % counter == 0:
            num_fact += 1

    return num_fact