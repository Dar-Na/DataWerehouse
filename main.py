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

    kontrolerzy = deps.readCSV("./data/Kontrolerzy.csv")
    print(kontrolerzy)

    # OKRES Z T2 DO T1
    start_date_one = datetime.date(2018, 1, 1)
    end_date_one = datetime.date(2020, 12, 31)

    # NUMBER OF PESELS
    num = 1500
    # GENERATE PESELS
    PESELS = pilot.generatePESELs(num=num, start_date=start_date_one, end_date=end_date_one)
    print(PESELS)
    save(PESELS, "T0-T1/PESELS.csv")
    # GENERATE PILOTS
    pilots = pilot.generatePilots(PESELs=PESELS, names=names, surnames=surnames)
    print(pilots)
    save(pilots, "T0-T1/pilots.csv")
    # GENERATE AIRPLANES
    samolots = samolot.generateSamolts(num=100)
    print(samolots)
    save(samolots, "T0-T1/samolots.csv")
    # GENERATE KURSES
    kurses = kurs.generateKurses(num=10)
    kurses = deps.delDuplicates(kurses)
    print(kurses)
    save(kurses, "T0-T1/kurses.csv")

    # CALCULATE TIME FROM ONE CITY TO ANOTHER
    times = deps.time(kurses)
    print(times)
    save(times, "T0-T1/times.csv")

    # GENERATE LOTY, AWARII AND PILOTÓW
    loty1, awarii, pilociWLocie = loty.generateLoty(
        num=6000, kurses=kurses, samolots=samolots, pilotes=pilots,
        times=times, start_date=start_date_one, end_date=end_date_one, kontrolerzy=kontrolerzy
    )
    save(loty1, "T0-T1/loty.csv")
    save(awarii, "T0-T1/awarii.csv")
    save(pilociWLocie, "T0-T1/pilociWLocie.csv")

    # OKRES Z T1 DO T2
    start_date_two = datetime.date(2021, 1, 1)
    end_date_two = datetime.date(2022, 12, 31)

    # NUMBER OF PESELS
    num = 4000
    # GENERATE PESELS
    PESELS2 = pilot.generatePESELs(num=num, start_date=start_date_two, end_date=end_date_two)
    print(PESELS2)
    save(PESELS + PESELS2, "T0-T2/PESELS.csv")

    # GENERATE PILOTS
    pilots2 = pilot.generatePilots(PESELs=PESELS2, names=names, surnames=surnames)
    print(pilots2)
    pilots, newName = pilot.changeName(pilots=pilots, names=names, surnames=surnames)

    # MERGE TABLES PILOTS
    PILOTS = pilots + pilots2
    save(PILOTS, "T0-T2/PILOTS.csv")
    save(newName, "newName.csv")

    # GENERATE AIRPLANES
    samolots2 = samolot.generateSamolts(num=150)
    print(samolots2)
    # MERGE TABLES AIRPLANES
    SAMOLOTS = samolots + samolots2
    save(SAMOLOTS, "T0-T2/samolots.csv")

    # GENERATE KURSES
    kurses2 = kurs.generateKurses(num=20)
    kurses2 = deps.delDuplicates(kurses2)
    print(kurses2)
    # MERGE TABLES KURSES
    KURSES = kurses + kurses2
    KURSES = KURSES
    save(KURSES, "T0-T2/kurses.csv")

    # CALCULATE TIME FROM ONE CITY TO ANOTHER
    times2 = deps.time(kurses2)
    print(times2)
    # MERGE TABLES TIME
    TIMES = times + times2
    # TIMES = list(dict.fromkeys(TIMES))
    save(TIMES, "T0-T2/times.csv")

    # GENERATE LOTY, AWARII AND PILOTÓW
    loty2, awarii2, pilociWLocie2 = loty.generateLoty(
        num=10000, kurses=KURSES, samolots=SAMOLOTS, pilotes=PILOTS,
        times=TIMES, start_date=start_date_one, end_date=end_date_one, kontrolerzy=kontrolerzy
    )

    save(loty1 + loty2, "T0-T2/loty.csv")
    save(awarii + awarii2, "T0-T2/awarii.csv")
    save(pilociWLocie + pilociWLocie2, "T0-T2/pilociWLocie.csv")