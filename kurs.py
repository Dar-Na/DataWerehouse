import random
import deps


def kurs(i):
    fCity = deps.cities[random.randrange(0, len(deps.LETTERS))]
    tCity = deps.cities[random.randrange(0, len(deps.LETTERS))]
    while(fCity == tCity):
        fCity = deps.cities[random.randrange(0, len(deps.LETTERS))]
        tCity = deps.cities[random.randrange(0, len(deps.LETTERS))]
    index = fCity[:3].upper() + "-" + tCity[:3].upper()
    name = fCity + "-" + tCity
    fCity = fCity + " lotnisko"
    tCity = tCity + " lotnisko"
    kurs = str(i + 1) + "," + index + "," + fCity + "," + tCity + "," + name
    print(kurs)
    return kurs

def generateKurses(num):
    arr = []
    for i in range(0, num):
        arr.append(kurs(i))

    return arr

