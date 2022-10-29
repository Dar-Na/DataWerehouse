import datetime
import geopy
from geopy import distance
import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
cities = ["Gdańsk", "Wrocław", "Warszawa", "Kraków", "Poznań", "Londyn", "Rzym", "Sztokholm", "Oslo", "Paryż",
          "Barcelona", "Kiruna", "Bruksela", "Evenes", "Helsinki", "Hamburg", "Kolonia", "Berlin", "Lipsk",
          "Kopenhaga", "Ateny", "Kalamata", "Sybin", "Praga", "Ostrawa", "Lublana", "Mumbaj", "Astana", "Hawana"]

def getAttr(str, ind1, ind2):
    index2 = findnth(str, ",", ind2-1)
    index1 = findnth(str, ",", ind1-1)
    return str[(index1+1):index2]

def findnth(haystack, needle, n):
    parts = haystack.split(needle, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(haystack) - len(parts[-1]) - len(needle)


def time(kurses):
    times = []
    geolocator = geopy.Nominatim(user_agent="Dar-Na")
    for i in range(0, len(kurses)):
        ind = findnth(kurses[i], ",", 3)
        str = kurses[i][ind+1::]
        fCity = str[:str.find("-")]
        tCity = str[(str.find("-")+1)::]
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
