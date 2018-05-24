#Score 100%
def solution(S):
    # write your code in Python 3.6
    length = len(S)

    if length == 0:
        return 1

    countL = 0

    for letter in S:
        if letter == "(":
            countL += 1
        else:
            countL -= 1

        if countL < 0:
            return 0

    if countL != 0:
        return 0

    return 1

string = '())'
print solution(string)


