#Score 100% (ale moc pokusu a dlouha doba)
##Find the smallest positive integer that does not occur in given sequence
def solution(A):
    # write your code in Python 3.6


    if len(A) < 1:
        return 1

    b = [x for x in A if x > 0]
    b.sort()

    length = len(b)
    num = 1

    for idx, i in enumerate(b):

        if num != i:
            return num

        if idx + 1 > length-1:
            if i != num:
               return num
            else:
                return num + 1

        elif i != b[idx+1]:
            num += 1

    return num







arr = [1,2,3]
print(solution(arr))