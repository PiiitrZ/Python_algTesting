import copy

def rotate(x):
    data = copy.deepcopy(x)

    ln = len(data) - 1

    for i in range(ln):
        for j in range(ln):
            data[i,j] = x[ln-j+1][i]

    print(data)


matr = [[1,2,3],
        [4,5,6],
        [7,8,9]]

rotate(matr)

lng = len(x) - 1

for idx_i, i in enumerate(x):
    for idx_y, y in enumerate(i):
        new_idx_y = lng - idx_i
        new_idx_i = lng - new_idx_y

        new_matr[new_idx_i][new_idx_y] = y
