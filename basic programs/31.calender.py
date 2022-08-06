import calendar
y=int(input("Enter year: "))
m=int(input("Enter month number: "))
c=calendar.TextCalendar(calendar.MONDAY)
cal=c.formatmonth(y,m)
print(cal)

'''
today's date

import datetime
print(datetime.date.today())
'''
