#Score 100 %
def solution(A):
    # write your code in Python 3.6


    lst = A[:]
    length = len(lst)

    if length == 1: return 0

    lst.sort()


    val_count = 1


    for idx, i in enumerate(lst):
        if idx < length - 1:
            nxt_idx = idx + 1

            if i == lst[nxt_idx]:
                val_count += 1
                if val_count > length / 2:
                    dominator = i
                    print (dominator)
                    index = A.index(dominator)
                    return index
            else:
                val_count = 1

    return -1



arr = [1]
#arr = [3,4,3,2,3,-1,3,3]
print(solution(arr))
