number = int(raw_input("Set integer: "))

def solution(N):
    binary = bin(N)
    print(binary)

    longest_gap = 0
    count = 0

#   Reseni hledani indexuu no.1(pres cyklus):
    """ lst_of_one = []
        for idx, c in enumerate(binary[2:]):      #najdi indexy jednotek
            if c == '1':
                lst_of_one.append(idx) """

#   Reseni hledani indexuu no.2 (pres list comprehension):
    lst_of_one = [idx for idx, val in enumerate(binary[2:]) if val == '1']

    print(lst_of_one)

    for idx, i in enumerate(lst_of_one):
        nxt_idx = idx + 1
        if nxt_idx < len(lst_of_one):              #kontrola konce pole
            count = lst_of_one[nxt_idx] - i - 1    #rozdil - 1 = velikost mezery
        if count > longest_gap:
            longest_gap = count

    return longest_gap

print(solution(number))