
def sum_sunday():
    weekday = 1
    sunday = 0
    for year in range(1900,2001):
        for month in range(1,13):
            day = 31
            if month == 4 or month == 6 or month == 9 or month == 11: day = 30 
            elif month == 2 and year % 4 == 0 and (year % 400 == 0 or year % 100 != 0): day = 29
            elif month == 2: day = 28   
            
            for i in range(1,day+1):
                if i == 1 and weekday == 7 and year > 1900: sunday += 1
                weekday+= 1
                if weekday == 8: weekday = 1
    return sunday

print(sum_sunday())
