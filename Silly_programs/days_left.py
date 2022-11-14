"""
Calculates the amount of days left of
school and what percentage of days we've
been through
3 options:
1. Find how many more days and weeks left until a certain date
2. Find what percentage of the distance you are
until a set date
3. Find what percentage of how many days left of school
(specific to Timpanogas in the 2022-2023 school year)
"""


def main():
    print('''
  Welcome!
  Would you like to:
  1. Find the distance between today and a future date
  2. Find percentage of of distance between 3 dates
  3. Find how much more school there is
  
  ''')
    i = int(input(">>> "))
    if i == 1:
        print("""
    Current date: 
    """)
        date1 = collect_date()
        print('''
    Future date:
    ''')
        date2 = collect_date()
        print(days_left(date1, date2))

    if i == 2:
        print('''
    Past date:
    ''')
        date1 = collect_date()
        print('''
    Current date:
    ''')
        date2 = collect_date()
        print('''
    Future date
    ''')
        date3 = collect_date()
        distance1 = days_left(date1, date3)
        distance2 = days_left(date2, date1)
        distance3 = 1 - (distance2 / distance1)
        distance3 *= 100
        distance3 = int(distance3)
        print(distance3)

    if i == 3:

        date1 = [8, 16, 2022]
        print('''
    Current date:
    ''')
        date2 = collect_date()
        date3 = [5, 26, 2023]
        distance1 = days_left(date1, date3)
        distance2 = days_left(date2, date3)
        distance3 = 1 - (distance2 / distance1)
        distance3 *= 100
        distance3 = int(distance3)
        print(str(distance3) + '% of school is over')
        print(str(distance2) + " days left in the school year")


def collect_date():
    # gets the year
    while True:
        year = int(input("Year: "))
        print()
        if year >= 0:
            break
        else:
            print("That's impossible, silly!")
            print()

    # gets the month
    while True:
        month = input("Month: ")
        print()
        month = what_month(month)
        if month <= 12:
            break
        else:
            print("That's not a month, silly!")
            print()

    # gets the day
    while True:
        day = int(input("Day: "))
        print()
        if day <= days_in_month(month, year) \
      and day >= 1:
            break
        else:
            print("That's impossible, silly!")
            print()
    return [month, day, year]


#The Nightmare Zone:
def days_left(begin, end):
    result = 0
    while True:
        if begin[1] != 0 and begin[0] != end[0]:
            result += days_in_month(begin[0], begin[2]) - begin[1]
            begin[1] = 0
            begin[0] += 1
        else:
            begin[1] = 0
        if begin[0] < 12 and begin[2] != end[2]:
            result += days_in_month(begin[0], begin[2])
            begin[0] += 1
        elif begin[0] < end[0] and begin[2] == end[2]:
            result += days_in_month(begin[0], begin[2])
            begin[0] += 1
        elif begin[0] == 12 and begin[2] != end[2]:
            result += days_in_month(begin[0], begin[2])
            begin[0] = 1
            begin[2] += 1
        elif begin[0] == end[0] and begin[2] == end[2]:
            result += end[1]
            break
    return result


# finds if a month in the year even exists
def what_month(month):
    if month == "January" or month == "january":
        return 1
    elif month == "February" or month == "february":
        return 2
    elif month == "March" or month == "march":
        return 3
    elif month == "April" or month == "april":
        return 4
    elif month == "May" or month == "may":
        return 5
    elif month == "June" or month == "june":
        return 6
    elif month == "July" or month == "july":
        return 7
    elif month == "August" or month == "august":
        return 8
    elif month == "September" or month == "september":
        return 9
    elif month == "October" or month == "october":
        return 10
    elif month == "November" or month == "november":
        return 11
    elif month == "December" or month == "december":
        return 12
    else:
        return 13


# finds if a day in a month is valid
def days_in_month(month, year):
    if month == 8:
        return 31
    elif is_even(month) == False and month != 2 and month < 8:
        return 31
    elif is_even(month) == False and month != 2 and month > 8:
        return 30
    elif is_even(month) and month != 2 and month > 8:
        return 31
    elif is_even(month) and month != 2 and month < 8:
        return 30
    elif month == 2 and year % 4 == 0:
        return 29
    elif month == 2:
        return 28
    else:
        return 489


# finds if a number is even
def is_even(num):
    if num % 2 == 0:
        return True
    return False


main()
