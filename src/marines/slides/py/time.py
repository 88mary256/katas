import datetime

months = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31,
          "September": 30, "October": 31, "November": 30, "December": 31}

leap_year = 1904


def days_in_month(month):
    return months[month]


def is_leap(year):
    return ((year - leap_year) % 4) == 0


def get_current_year():
    now = datetime.datetime.now()
    return now.year


def get_current_month():
    now = datetime.datetime.now()
    return now.month


def get_current_day():
    now = datetime.datetime.now()
    return now.day


def get_current_minute():
    now = datetime.datetime.now()
    return now.minute


def get_current_second():
    now = datetime.datetime.now()
    return now.second


'''
Create 1 module to Calculate age in minutes, hours and days
Create 1 module to print 4 different messages :
You are a child, when the age is lower than 12
Your are teenager, when the age is between 13 and 17
You are young, when the age is between 18 and 29
You are adult, when the age is greater than 30
'''


def get_age_in_days(age):
    return int(age) * 365


def get_age_in_hr(age):
    return get_age_in_days(age) * 24


def get_age_in_min(age):
    return get_age_in_hr(age) * 60


def what_am_I(age):
    if (age == None or age < 0): print "Error, invalid age"
    if (age <= 12): print "You are child"
    if (age > 12 and age <= 17): print "Your are teenager"
    if (age > 17 and age <= 29): print "You are young"
    if (age > 29): print "You are adult"
