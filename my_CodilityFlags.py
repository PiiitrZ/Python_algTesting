#Score 40% (Correctness 75%, Performance 0%)
def solution(A):
    # write your code in Python 3.6
    length = len(A)
    if length < 3:
        return 0

    flg_cnt = 0
    last_flag_idx = 0

    for idx, i in enumerate(A):

        if idx - 1 >= 0 and idx + 1 != length: #no first no last

            if A[idx-1] < i and i > A[idx+1]:  #peak


                if flg_cnt == 0 or \
                    (idx - last_flag_idx - 1) >= flg_cnt: #if no flag or if distance OK

                    last_flag_idx = idx
                    flg_cnt += 1

    return flg_cnt

#arr = [1,5,3,4,3,4,1,2,3,4,6,2]
arr = [1,3,2]
print(solution(arr))
