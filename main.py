import datetime
import pilot
import deps
import samolot
import kurs
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
    end_date = datetime.date(2020, 12, 31)
    num = 1500
    PESELS = pilot.generatePESELs(num=num, start_date=start_date, end_date=end_date)
    print(PESELS)

    pilots = pilot.generatePilots(PESELs=PESELS, names=names, surnames=surnames)
    print(pilots)

    samolots = samolot.generateSamolts(num=100)
    print(samolots)

    kurses = kurs.generateKurses(num=100)
    print(kurses)

    save(names, "names.csv")
    save(surnames, "surnames.csv")
    save(PESELS, "PESELS.csv")
    save(pilots, "pilots.csv")
    save(samolots, "samolots.csv")
    save(kurses, "kurses.csv")
