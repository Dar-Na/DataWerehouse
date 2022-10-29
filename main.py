import datetime
import pilot
import deps
import samolot
import kurs
import loty
import pandas as pd

def save(arr, path):
    df = pd.DataFrame(arr)
    df.to_csv("./data/" + path, index=False)

if __name__ == "__main__":
    names = deps.parse("names.txt")
    print(names)
    print(len(names))

    surnames = deps.parse("surnames.txt")
    print(surnames)

    start_date = datetime.date(2019, 1, 1)
    end_date_one = datetime.date(2020, 12, 31)

    num = 1500
    PESELS = pilot.generatePESELs(num=num, start_date=start_date, end_date=end_date_one)
    print(PESELS)

    pilots = pilot.generatePilots(PESELs=PESELS, names=names, surnames=surnames)
    print(pilots)

    samolots = samolot.generateSamolts(num=100)
    print(samolots)

    kurses = kurs.generateKurses(num=60)
    print(kurses)

    times = deps.time(kurses)
    print(times)

    loty, awarii, pilociWLocie = loty.generateLoty(num=6000, kurses=kurses, samolots=samolots, pilotes=pilots, times=times, start_date=start_date, end_date=end_date_one)
    # print(loty)
    # print(awarii)
    # print(pilociWLocie)

    save(PESELS, "PESELS.csv")
    save(pilots, "pilots.csv")
    save(samolots, "samolots.csv")
    save(kurses, "kurses.csv")
    save(times, "times.csv")
    save(loty, "loty.csv")
    save(awarii, "awarii.csv")
    save(pilociWLocie, "pilociWLocie.csv")
