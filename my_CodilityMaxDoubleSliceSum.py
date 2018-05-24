#score 38% (Correctness 83%, Performance 0%)
def solution(A):
    # write your code in Python 3.6
    length = len(A)
    max_sum = min(A)

    if length == 1:
        return A[0]

    for x in range(0,length-2):
        for y in range(x+1, length-1):
            for z in range(y+1, length):

                sum = get_ds_sum(A, x, y, z)
                if sum > max_sum:
                    max_sum = sum
    return max_sum

def get_ds_sum(A, x, y, z):
    # sum = A[x+1] + A[x+2] +...+ A[y-1] + A[y+1] + A[y+2] +...+ A[z-1]
    sum = 0

    counter = x + 1
    while counter <= y - 1:
        sum += A[counter]
        counter += 1

    counter = y + 1
    while counter <= z - 1:
        sum += A[counter]
        counter += 1

    return sum

arr = [3,2,6,-1,4,5,-1,2]
#arr = [5,5,5] #pry by melo vyjit 0 - nevim jak (ostatni test. pripady prosli)
print(solution(arr))