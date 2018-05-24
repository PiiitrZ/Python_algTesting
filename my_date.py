name = raw_input("your name: ")
age = raw_input("your age: ")

def get_100a_year(iv_age):
    diff = 100 - int(iv_age)

    import datetime

    now = datetime.datetime.now()
    res = now.year + diff

    return res

year_turn100 = get_100a_year(age)

print("You, %s, will turn 100 in year %i" % (name, year_turn100))
