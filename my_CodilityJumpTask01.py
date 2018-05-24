def solution(A, B):
    # write your code in Python 3.6
    strB = str(B)
    strA = str(A)

    res = []

    strLenA = len(strA)
    strLenB = len(strB)

    if strLenA == strLenB:
        if strA == strB:
            return 0
        else:
            return -1
    else:
        for i in range(strLenB - 1):
            endStr = i + strLenA

            strNum = strB[i:endStr]

            if strNum == strA:
                res.append(i)

    if len(res) == 0:
        res.append(-1)

    return res[0]

    """
    if len(res) == 1:   #nalezeno jednou
        return res[0]
    else:               #nalezeno vickrat
        return res
    """
    # return strB.find(strA)



print(solution(535, 53578653532))