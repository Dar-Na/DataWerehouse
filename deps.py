import datetime
import geopy
from geopy import distance
import random
import csv
from itertools import groupby

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
cities = ["Wrocław", "Warszawa", "Kraków", "Poznań", "Londyn", "Rzym", "Sztokholm", "Oslo", "Paryż",
          "Barcelona", "Kiruna", "Bruksela", "Evenes", "Helsinki", "Hamburg", "Kolonia", "Berlin", "Lipsk",
          "Kopenhaga", "Ateny", "Kalamata", "Sybin", "Praga", "Ostrawa", "Lublana", "Mumbaj", "Astana", "Hawana"]

klassyArr = ["biznesowa", "zwykła", "ekonomiczna"]

def getAttr(str, ind1, ind2):
    index2 = findnth(str, ",", ind2-1)
    index1 = findnth(str, ",", ind1-1)
    return str[(index1+1):index2]

def findnth(haystack, needle, n):
    parts = haystack.split(needle, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(haystack) - len(parts[-1]) - len(needle)

def delDuplicates(array):
    return [max(g) for _, g in groupby(array, lambda x: x[0])]

def time(kurses):
    times = []
    geolocator = geopy.Nominatim(user_agent="Dar-Na")
    for i in range(0, len(kurses)):
        str = kurses[i][3]
        str = str.split("-")
        fCity = str[0]
        tCity = str[1]
        try:
            fCityLocation = geolocator.geocode(fCity)
            tCityLocation = geolocator.geocode(tCity)
        except:
            fCityLocation = geolocator.geocode(fCity)
            tCityLocation = geolocator.geocode(tCity)
        dist = distance.geodesic(
            (fCityLocation.latitude, fCityLocation.longitude),
            (tCityLocation.latitude, tCityLocation.longitude)
        ).km
        # airplane speed
        v = random.randrange(740, 900)
        # time in hours
        time = dist / v
        print([fCity, tCity, time, dist, v])
        times.append([fCity, tCity, time])
    return times

def readCSV(file):
    data = []
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def parse(file):
    temp = open(file, "r")
    temp = temp.readlines()
    str = ""
    for t in temp:
        t = t.replace('\n', ' ')
        str += t
    arr = str.split()
    return arr


def randomDate(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date
