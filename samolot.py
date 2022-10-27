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
        arr.append(index())

    return arr


def generateSamolts(num):
    samolots = []
    types = [
        "Turboprop Aircraft", "Piston Aircraft", "Light Jet",
        "Mid-Size Jet", "Jumbo Jet", "Regional Jet",
        "Narrow Body Aircraft", "Wide Body Airliners", "Regional",
        "Commuter liner", "Airbus"
    ]
    indexes = generateIndexes(num)
    for i in range(0, num):
        index = indexes[i]
        year = random.randrange(1911, 2022)
        type = types[random.randrange(0, len(types))]
        samolot = str(i + 1) + "," + str(index) + "," + type + "," + str(year)
        print(samolot)
        samolots.append(samolot)

    return samolots