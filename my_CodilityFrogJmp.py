
def solution(X, Y, D):
    # write your code in Python 3.6
    distance = Y - X

    if distance == 0:
        num_jmps = 0

    elif distance > 0:
        num_jmps = distance // D
        if distance % D > 0:
            num_jmps += 1

    return num_jmps


print(solution(5, 5, 30))