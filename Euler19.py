__author__ = 'adam'

class Time:
    month = 1
    year = 1901
    weekday = 0

Time.weekday += 365 % 7
print 365 % 7
def tellTime():
    print Time.month, Time.year, Time.weekday

tellTime()

count=0
while Time.year < 2001:
    if Time.month == 2:
        if Time.year%4 == 0 and (Time.year%100 != 0 or Time.year%400==0):
            Time.weekday = (Time.weekday+29%7)%7
    elif Time.month ==4 or Time.month ==6 or Time.month == 9 or Time.month==11:
        Time.weekday = (Time.weekday+30%7)%7
    else:
        Time.weekday = (Time.weekday+31%7)%7
    if Time.weekday == 6:
        count+=1
    Time.month+=1
    if Time.month == 13:
        Time.month=1
        Time.year+=1
        tellTime()
print count
tellTime()
Time.year=1904
print Time.year%4 == 0 and (Time.year%100 != 0 or Time.year%400==0)