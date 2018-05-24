#Score: 69% (Correctness 100%, Performance 20%)
def solution(A):
    # write your code in Python 3.6
    max_sum = min(A)
    length = len(A)

    if length == 1:
        return A[0]

    for i in range(0, length):
        for y in range(i, length):

            sum = get_ds_sum(A, i, y)
            if sum > max_sum:
                max_sum = sum
                print(i,y)

    return max_sum

def get_ds_sum(A, p, q):
    sum = 0

    counter = p
    while counter <= q:
        sum += A[counter]
        counter += 1

    return sum


arr = [3,2,-6,4,0]
#arr = [-2,-2]
#get_ds_sum(arr, 0,2)
print(solution(arr))