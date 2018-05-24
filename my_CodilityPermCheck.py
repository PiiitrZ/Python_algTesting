#kontrola permutac (A permutation is a sequence containing each element from 1 to N once, and only once.)
def solution(A):
    # write your code in Python 3.6
    lngth = len(A)

    my_arr = A[:]
    my_arr.sort()

    for i in range(lngth):

        if my_arr[i] != i+1:
            return 0

    return 1

arr = [4,1,3]
print(solution(arr))
