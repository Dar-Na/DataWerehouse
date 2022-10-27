import datetime
import random

LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

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