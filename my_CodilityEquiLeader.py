#Score: 55% (Correctness 100%, Performance 0%)
#Performance: expected O(N), detected O(N**2}
def solution(A):
    # write your code in Python 3.6

    length = len(A)
    res_count = 0

    counter = 0

    while counter < length:
        counter += 1

        leftSideLeader = find_leader(A[:counter])
        if leftSideLeader != None:
            rightSideLeader = find_leader(A[counter:])
            if rightSideLeader != None:
                if leftSideLeader == rightSideLeader:
                    res_count += 1

    return res_count


def find_leader(B):
    length = len(B)

    if length == 1: return B[0]

    b_sort = B[:]
    b_sort.sort()

    max_count = 0


    for idx, i in enumerate(b_sort):
        if idx == 0:
            count = 1
        elif i == b_sort[idx - 1]:
            count += 1
        else:
            count = 1

        if count > max_count:
            max_count = count
            leader = i

    if max_count > (length / 2):
        return leader



#arr = [0,1,1,1]
arr = [4,3,4,4,4,2]
print(solution(arr))