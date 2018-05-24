#Score 80% (Correctness 100%, Performance 60%)
import math

def solution(N):
    sq = math.floor(math.sqrt(N))

    a = sq
    b = sq

    tim = a * b

    while tim != N:
        if tim < N:
            a += 1
            while N % a != 0:
                a += 1
        if tim > N:
            b -= 1
            while N % b != 0:
                b -= 1

        if b == 1:
            a = N

        tim = a * b

    perimeter = 2*(a + b)


    return perimeter


area = 7

print(solution(area))