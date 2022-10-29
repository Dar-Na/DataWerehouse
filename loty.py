import datetime
import random
from datetime import timedelta
import deps

def awaria(samolotZastepczy, samolotAwaria):
    index = samolotZastepczy + "-" + samolotAwaria + "-" + \
            deps.LETTERS[random.randrange(0, len(deps.LETTERS))].upper() + \
            deps.LETTERS[random.randrange(0, len(deps.LETTERS))].upper() + \
            deps.LETTERS[random.randrange(0, len(deps.LETTERS))].upper()
    return index

def generateLoty(num, kurses, samolots, pilotes, times, start_date, end_date):
    loty = []
    pilociWLocie = []
    awarii = []
    for i in range(0, num):
        kursId = random.randrange(0, len(kurses))
        kurs = deps.getAttr(kurses[kursId], 1, 2)
        samolot = deps.getAttr(samolots[random.randrange(0, len(samolots))], 1, 2)
        pilot1 = deps.getAttr(pilotes[random.randrange(0, len(pilotes))], 1, 2)
        pilot2 = deps.getAttr(pilotes[random.randrange(0, len(pilotes))], 1, 2)
        while (pilot1 == pilot2):
            pilot1 = deps.getAttr(pilotes[random.randrange(0, len(pilotes))], 1, 2)
            pilot2 = deps.getAttr(pilotes[random.randrange(0, len(pilotes))], 1, 2)
        boardingTime = random.randrange(20, 300)
        kontroler = "NaN"
        idAwarii = ""
        klasaLotu = "NaN"
        if random.randrange(0, 11) > 9:
            samolotAwaria = deps.getAttr(samolots[random.randrange(0, len(samolots))], 1, 2)
            while (samolot == samolotAwaria):
                samolot = deps.getAttr(samolots[random.randrange(0, len(samolots))], 1, 2)
                samolotAwaria = deps.getAttr(samolots[random.randrange(0, len(samolots))], 1, 2)
            idAwarii = awaria(samolot, samolotAwaria)
            awarii.append(idAwarii + "," + samolot + "," + samolotAwaria)
        tmpTime = deps.randomDate(start_date=start_date, end_date=end_date)
        tmpTime = datetime.datetime(tmpTime.year, tmpTime.month, tmpTime.day, 0, 0, 0)
        oczekiwanyCzasR = tmpTime + timedelta(hours=random.randrange(0, 23), minutes=random.randrange(0, 59), seconds=random.randrange(0, 59))
        oczekiwanyCzasZ = oczekiwanyCzasR + timedelta(hours=times[kursId][2])
        opz = 0
        if boardingTime > 40:
            opz = boardingTime - 40
        rzeczywistyCzasR = oczekiwanyCzasR + timedelta(minutes=opz)
        opz = opz + random.randrange(0, 15)
        rzeczywistyCzasZ = oczekiwanyCzasZ + timedelta(minutes=opz)
        pilociWLocie.append(pilot1 + "," + pilot2 + "," + kurs + "," + samolot + "," + str(rzeczywistyCzasR.ctime()))
        loty.append(
            kurs + "," + samolot + "," + str(rzeczywistyCzasR.ctime()) + ","
            + str(rzeczywistyCzasZ.ctime()) + "," + str(oczekiwanyCzasZ.ctime()) + "," + str(oczekiwanyCzasR.ctime())
            + "," + idAwarii + "," + str(boardingTime) + "," + klasaLotu + "," + kontroler
        )

    #print(loty)
    print("####")
    print("####")
    print("####")
    print("####")
    print("####")
    print("####")
    print("####")
    print("####")
    print("####")
    print("####")
    #print(awarii)
    print("####")
    print("####")
    print("####")
    print("####")
    print("####")
    print("####")
    print("####")
    print("####")
    print("####")
    print("####")
    #print(pilociWLocie)

    return loty, awarii, pilociWLocie