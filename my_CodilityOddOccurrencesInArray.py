arr = [9, 3, 9, 3, 9, 7, 9]

def solution(A):
    # write your code in Python 3.6
    dict = {}
    for i in A:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for item in dict:
        if dict[item] == 1:
            return item


print(solution(arr))


