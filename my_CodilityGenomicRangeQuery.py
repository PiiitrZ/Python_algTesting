#score 62% (Correctness 100%, Performance 0% :D)
def solution(S, P, Q):
    # write your code in Python 3.6

    def get_impactF(s, i):
        dict = {'A': 1, 'C': 2, "G": 3, "T": 4}

        nucleotid = s[i]
        return dict[nucleotid]

    result = []
    length = len(P)

    for i in range (length):
        valP = P[i]
        valQ = Q[i]

        if valP == valQ:
            min_impF = get_impactF(S, valP)

        else:
            min_impF = 4

            for y in range(valP, valQ+1):
                impactF = get_impactF(S, y)

                if impactF < min_impF:
                    min_impF = impactF

        result.append(min_impF)

    return result






arrP = [2,5,0]
arrQ = [4,5,6]
strS = 'CAGCCTA'

print(solution(strS, arrP, arrQ))