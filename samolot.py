import random
import deps

# airplane types https://an.aero/different-types-of-airplanes/

def index():
    index = deps.LETTERS[random.randrange(0, len(deps.LETTERS))].upper() + \
            deps.LETTERS[random.randrange(0, len(deps.LETTERS))].upper() + \
            deps.LETTERS[random.randrange(0, len(deps.LETTERS))].upper() + str(random.randrange(100, 999))
    print(index)
    return index

def generateIndexes(num):
    arr = []
    for _ in range(0, num):
        ind = index()
        while ind in arr:
            ind = index()
        arr.append(ind)

    return arr


def generateSamolts(num):
    samolots = []
    sO = []
    types = [
        "Turboprop Aircraft", "Piston Aircraft", "Light Jet",
        "Mid-Size Jet", "Jumbo Jet", "Regional Jet",
        "Narrow Body Aircraft", "Wide Body Airliners", "Regional",
        "Commuter liner", "Airbus"
    ]
    indexes = generateIndexes(num)
    for i in range(0, num):
        index = indexes[i]
        klasaLotu = deps.klassyArr[random.randrange(0, len(deps.klassyArr))]
        year = random.randrange(1911, 2022)
        type = types[random.randrange(0, len(types))]
        while sO.__contains__([type, str(year)]):
            year = random.randrange(1911, 2022)
            type = types[random.randrange(0, len(types))]
        samolot = str(i + 1) + "," + str(index) + "," + type + "," + str(year)
        print(samolot)
        samolots.append([str(index), type, str(year), klasaLotu])
        sO.append([type, str(year)])

    return samolots