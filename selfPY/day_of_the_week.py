import calendar

date = input("Enter a date: ")

day, month, year = map(int, date.split('/'))

weekday_num = calendar.weekday(year, month, day)
weekday_name = calendar.day_name[weekday_num]
print(weekday_name)