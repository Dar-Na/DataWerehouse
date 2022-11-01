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
    # PARSE NAMES AND SURNAMES FROM TXT FILE
    names = deps.parse("names.txt")
    print(names)
    print(len(names))

    surnames = deps.parse("surnames.txt")
    print(surnames)

    # OKRES Z T2 DO T1
    start_date_one = datetime.date(2019, 1, 1)
    end_date_one = datetime.date(2020, 12, 31)

    # NUMBER OF PESELS
    num = 1500
    # GENERATE PESELS
    PESELS = pilot.generatePESELs(num=num, start_date=start_date_one, end_date=end_date_one)
    print(PESELS)
    # GENERATE PILOTS
    pilots = pilot.generatePilots(PESELs=PESELS, names=names, surnames=surnames)
    print(pilots)
    # GENERATE AIRPLANES
    samolots = samolot.generateSamolts(num=100)
    print(samolots)
    # GENERATE KURSES
    kurses = kurs.generateKurses(num=30)
    print(kurses)
    # CALCULATE TIME FROM ONE CITY TO ANOTHER
    times = deps.time(kurses)
    print(times)
    # GENERATE LOTY, AWARII AND PILOTÓW
    loty1, awarii, pilociWLocie = loty.generateLoty(
        num=6000, kurses=kurses, samolots=samolots, pilotes=pilots,
        times=times, start_date=start_date_one, end_date=end_date_one
    )

    # OKRES Z T1 DO T2
    start_date_two = datetime.date(2021, 1, 1)
    end_date_two = datetime.date(2021, 12, 31)

    # NUMBER OF PESELS
    num = 4000
    # GENERATE PESELS
    PESELS2 = pilot.generatePESELs(num=num, start_date=start_date_two, end_date=end_date_two)
    print(PESELS2)
    # GENERATE PILOTS
    pilots2 = pilot.generatePilots(PESELs=PESELS2, names=names, surnames=surnames)
    print(pilots2)
    # MERGE TABLES PILOTS
    PILOTS = pilots + pilots2
    # GENERATE AIRPLANES
    samolots2 = samolot.generateSamolts(num=150)
    print(samolots2)
    # MERGE TABLES AIRPLANES
    SAMOLOTS = samolots + samolots2
    # GENERATE KURSES
    kurses2 = kurs.generateKurses(num=50)
    print(kurses2)
    # MERGE TABLES KURSES
    KURSES = kurses + kurses2
    # CALCULATE TIME FROM ONE CITY TO ANOTHER
    times2 = deps.time(kurses2)
    print(times2)
    # MERGE TABLES TIME
    TIMES = times + times2
    # GENERATE LOTY, AWARII AND PILOTÓW
    loty2, awarii2, pilociWLocie2 = loty.generateLoty(
        num=10000, kurses=KURSES, samolots=SAMOLOTS, pilotes=PILOTS,
        times=TIMES, start_date=start_date_one, end_date=end_date_one
    )

    # CHANGE NAMES AND SURNAMES
    newNames = pilot.changeName(PESELs=PESELS + PESELS2, names=names, surnames=surnames)

    save(PESELS + PESELS2, "PESELS.csv")
    save(PILOTS, "pilots.csv")
    save(SAMOLOTS, "samolots.csv")
    save(KURSES, "kurses.csv")
    save(TIMES, "times.csv")
    save(loty1 + loty2, "loty.csv")
    save(awarii + awarii2, "awarii.csv")
    save(pilociWLocie + pilociWLocie2, "pilociWLocie.csv")
    save(newNames, "newNames.csv")