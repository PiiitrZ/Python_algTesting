#Score 90% (Correctness 90%, Performance N/A)
#T = 1, F = 0. cisla reverzne -> provest bin soucet
# vysledek prevest zpet na znaky reverzne

def solution(S,T):
    binS = transl_to_bin(S)
    binT = transl_to_bin(T)

    sum = bin(int(binS,2) + int(int(binT,2)))
    return(transl_to_str(sum))


def transl_to_bin(string):
    new_str = ""

    if string == "":
        return '0'

    for s in string[::-1]:
        if s == "T":
            new_str += "1"
        if s == "F":
            new_str += "0"

    return new_str

def transl_to_str(bin):
    new_str = ""
    for i in bin[::-1]:
        if i == 'b':
            break
        if i == "1":
            new_str += "T"

        if i == "0":
            new_str += "F"

    return new_str


strS = 'FFT'
strT = 'TT'
print( solution(strS,strT))