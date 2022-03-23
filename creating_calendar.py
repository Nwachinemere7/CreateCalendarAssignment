#importing the calendar module
import calendar as cal

#parameters:

year = 2005
month = 8           #index for the month of August

#this line changes the starting day to sunday on my calendar.

s_day = cal.TextCalendar(cal.SUNDAY)
starting_day = s_day.formatmonth(year, month)

print(starting_day)
print(cal.calendar(year))