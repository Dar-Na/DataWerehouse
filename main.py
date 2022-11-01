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

    # OKRES Z T2 DO T1

    start_date_one = datetime.date(2019, 1, 1)
    end_date_one = datetime.date(2020, 12, 31)

    num = 1500
    PESELS = pilot.generatePESELs(num=num, start_date=start_date_one, end_date=end_date_one)
    print(PESELS)

    pilots = pilot.generatePilots(PESELs=PESELS, names=names, surnames=surnames)
    print(pilots)

    samolots = samolot.generateSamolts(num=100)
    print(samolots)

    kurses = kurs.generateKurses(num=60)
    print(kurses)

    times = deps.time(kurses)
    print(times)

    loty1, awarii, pilociWLocie = loty.generateLoty(
        num=6000, kurses=kurses, samolots=samolots, pilotes=pilots,
        times=times, start_date=start_date_one, end_date=end_date_one
    )

    # OKRES Z T1 DO T2

    start_date_two = datetime.date(2021, 1, 1)
    end_date_two = datetime.date(2021, 12, 31)

    num = 4000
    PESELS2 = pilot.generatePESELs(num=num, start_date=start_date_two, end_date=end_date_two)
    print(PESELS)

    pilots2 = pilot.generatePilots(PESELs=PESELS, names=names, surnames=surnames)
    print(pilots)

    samolots2 = samolot.generateSamolts(num=150)
    print(samolots)

    kurses2 = kurs.generateKurses(num=120)
    print(kurses)

    times2 = deps.time(kurses)
    print(times)

    loty2, awarii2, pilociWLocie2 = loty.generateLoty(
        num=10000, kurses=kurses, samolots=samolots, pilotes=pilots,
        times=times, start_date=start_date_one, end_date=end_date_one
    )

    # CHANGE NAMES AND SURNAMES
    newNames = pilot.changeName(PESELs=PESELS + PESELS2, names=names, surnames=surnames)

    save(PESELS + PESELS2, "PESELS.csv")
    save(pilots + pilots2, "pilots.csv")
    save(samolots + samolots2, "samolots.csv")
    save(kurses + kurses2, "kurses.csv")
    save(times + times2, "times.csv")
    save(loty1 + loty2, "loty.csv")
    save(awarii + awarii2, "awarii.csv")
    save(pilociWLocie + pilociWLocie2, "pilociWLocie.csv")
    save(newNames, "newNames.csv")