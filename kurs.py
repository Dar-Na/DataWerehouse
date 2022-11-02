import random
import deps


def kurs(i):
    fCity = "Gdańsk"
    tCity = deps.cities[random.randrange(0, len(deps.LETTERS))]
    index = fCity[:3].upper() + "-" + tCity[:3].upper()
    name = fCity + "-" + tCity
    fCity = fCity + " lotnisko"
    fCity2 = tCity
    tCity = tCity + " lotnisko"
    tCity2 = "Gdańsk"
    index2 = fCity2[:3].upper() + "-" + tCity2[:3].upper()
    name2 = fCity2 + "-" + tCity2
    fCity2 = fCity2 + " lotnisko"
    tCity2 = tCity2 + " lotnisko"
    return [index, fCity, tCity, name], [index2, fCity2, tCity2, name2]

def generateKurses(num):
    arr = []
    n = int(num / 2)
    for i in range(0, n):
        f, t = kurs(i)
        while f in arr:
            f, t = kurs(i)
        arr.append(f)
        arr.append(t)

    return arr

