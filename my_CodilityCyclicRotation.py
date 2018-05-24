arr = [1,2,3,4,5,6,7,8,9]
loops = 3


def solution(A, K):

    result = A[:]  # type: object

    if A == []:
        return A

    for i in range(K):          #pocet otoceni
        result_tmp = result[:]  #odlozit vysledek predchoziho otoceni
        result = []             #clear vysledku

        last = len(result_tmp) - 1
        result.append(result_tmp[last]) #posledni na prvni misto

        for idx, item in enumerate(result_tmp): #otoceni"
            if idx < len(A) - 1:    # opakovat do PREDposledni polozky
                result.append(result_tmp[idx])

    return result

print(arr)
print(solution(arr, loops))