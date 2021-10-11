#TatiyanaHicks
#Course:151,Prof.Mehri
#Date 10/06/202
#Programming assignment
#Program inputs (month 1 -12 and year)
#Program Outputs (number of days in the month)


year = 2000
if (year % 4 ) == 0:
    if (year % 100 ) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year" .format(year))
        else:
            print("{0} is not a leap year" . format(year))
    else:
        print ("{0} is a leap year" . format(year))
else:
    print("{0} is not a leap year". format(year))

print("please input the number of days in the month:")
month = (input("please write a month (1-12): "))
year = (input("please write a year (1800-2099): "))

leap_year = 0
if month == (1, 3, 5, 7, 8, 10, 12):
    print("there are 31 days in month")
elif month == (4, 6, 9, 11):
    print("there are 30 days in month")
elif leap_year : #2
     print('there are 29 days in month if it is a leap year')
else:
    print("there are 28 days in month")