#score = 54% (correctness = 100%, performance = 0%!!??)
def solution(X, A):
    # write your code in Python 3.6
    time = 0

    for pos in range(1, X+1): #pozice
        try:
            sec = A.index(pos)
        except: #pozice nenalezena - konec
            return -1

        if time == 0:
            time = sec
        elif time < sec:
            time += sec - time

    return time



arr = [1,3,1,4,2,3,5,4]

print(solution(5, arr))



