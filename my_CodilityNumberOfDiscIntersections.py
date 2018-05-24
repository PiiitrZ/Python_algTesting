#Score 50% (Correctness 100%, Performance 0%)
def solution(A):
    # write your code in Python 3.6
    num_pairs = 0
    pairs = []

    for cent1, rad1 in enumerate(A):
        for cent2, rad2 in enumerate(A):
            if cent1 != cent2:
                pair = [cent1, cent2]
                pair.sort()

                if pair not in pairs:
                    distance = abs(cent2 - cent1)
                    sum_rad = rad1 + rad2

                    if distance <= sum_rad:
                        pairs.append(pair)
                        num_pairs += 1
    return num_pairs


arr = [0, 0, 2]
print(solution(arr))
