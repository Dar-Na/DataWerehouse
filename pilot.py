import random
import deps

def generatePESELs(num, start_date, end_date):
    PESELS = []

    for _ in range(0, num):
        n = PESEL(deps.randomDate(start_date, end_date))
        PESELS.append(n)

    return PESELS

def generatePilots(PESELs, names, surnames):
    arr = []
    for i in range(0, len(PESELs)):
        pesel = PESELs[i]
        name = names[random.randrange(0, len(names))]
        if i % 2 == 0:
            surname = surnames.pop(random.randrange(0, len(surnames)))
        else:
            surname = surnames[random.randrange(0, len(surnames))]
        pilot = str(i+1) + "," + str(pesel) + "," + name + "," + surname
        print(pilot)
        arr.append(pilot)

    return arr

def PESEL(random_date):
    year = random_date.year
    month = random_date.month
    day = random_date.day
    if year > 2000:
        month += 20

    four_random = random.randint(1000, 9999)
    four_random = str(four_random)

    # here comes the equation part, it calculates the last digit

    y = '%02d' % (year % 100)
    m = '%02d' % month
    dd = '%02d' % day

    a = y[0]
    a = int(a)

    b = y[1]
    b = int(b)

    c = m[0]
    c = int(c)

    d = m[1]
    d = int(d)

    e = dd[0]
    e = int(e)

    f = dd[1]
    f = int(f)

    g = four_random[0]
    g = int(g)

    h = four_random[1]
    h = int(h)

    i = four_random[2]
    i = int(i)

    j = four_random[3]
    j = int(j)

    check = a + 3 * b + 7 * c + 9 * d + e + 3 * f + 7 * g + 9 * h + i + 3 * j

    if check % 10 == 0:
        last_digit = 0
    else:
        last_digit = 10 - (check % 10)

    # printing the final number out

    print('%02d' % (year % 100), end='')
    print('%02d' % month, end='')
    print('%02d' % day, end='')
    print(four_random, end='')
    print(last_digit)

    num = (year % 100) * 1000000000 + month * 10000000 + day * 100000 + int(four_random) * 10 + last_digit
    return num