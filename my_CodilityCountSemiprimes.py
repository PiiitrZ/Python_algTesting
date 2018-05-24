#Score 55% (Correctness 100%, Performance 20%)
def solution(N, P, Q):
    # write your code in Python 3.6

    length = len(P)
    result = [0]*length

    for i in range(length):
        count_prime = 0
        for y in range(P[i], Q[i] + 1):
            if is_semi_prime(y) == True:
                count_prime += 1
        result[i] = count_prime

    return result


def is_semi_prime(x):
     if x < 4:
        return False

     if is_prime(x) == True:
         return False

     for i in range(2,x):
         if x % i == 0 and is_prime(i) != True:
             return False

     return True


def is_prime(x):

    if x == 0 or x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True





num = 26
arrP = [1,4,16]
arrQ = [26,10,20]
print(solution(num, arrP, arrQ))