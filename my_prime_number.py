num_to_check = int(raw_input("Prime number: "))


def check_prime_num(iv_num):
    if iv_num == 0 or iv_num == 1:
        result = {"res": False}
        return result

    for i in range((iv_num / 2) +1):   # type: int

        if i <> 0 and i <> 1 and i <> iv_num:

            if iv_num % i == 0:
                result = {"res": False, "div": i}
                return result

    result = {"res": True}
    return result


result = check_prime_num(num_to_check)


if result['res'] == True:
    print("%i is prime number" % num_to_check)
elif num_to_check == 0 or num_to_check == 1:
    print ("%i is NOT prime number." % (num_to_check))
else:
    print ("%i is NOT prime number. Is dividable by %i" % (num_to_check, int(result['div'])))
