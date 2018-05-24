#Score: 100% (Performance N/A)
#Zadani: komprimuj text -> vice nez 1 znak v retezci za sebou = (2+znak)

def solution(S):
    # write your code in Python 3.6
    seq_length = 0
    new_str = ""
    length = len(S)

    for idx, s in enumerate(S):
        if idx + 1 != length:

            if s == S[idx+1]:   #spocitej pocet znaku za sebou
                seq_length += 1

            elif seq_length >= 1:   #novy znak, pocet znaku vic nez 1
                seq_length += 1

                new_str += str(seq_length)  #zapis
                new_str += s
                seq_length = 0  #vynulovat

            else:
                new_str += s   #novy znak, pocet znaku predchoziho max 1

        else: #osetreni konce stringu
            if seq_length + 1 > 1:
                new_str += str(seq_length + 1)

            new_str += S[length-1]

    return new_str




st = "bbgggtt222"
#st = "bb"
print(solution(st))