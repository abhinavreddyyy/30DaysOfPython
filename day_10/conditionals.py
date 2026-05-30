calendar = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
            'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

month = input("Enter month: ").lower()

if month in calendar:

    position = calendar.index(month)

    if month == 'feb':
        days = 28

    if position <= 7 and position % 2 == 1:
            days = 31
    else:
            days = 30

    if position % 2 == 0:
            days = 31
    else:
            days = 30

    print("number of days in", month, "is", days)

else:
    print("Invalid month")