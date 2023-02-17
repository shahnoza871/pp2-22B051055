#1 Write a Python program to subtract five days from current date.
"""from datetime import datetime, timedelta
print(datetime.now() - timedelta(days = 5))
"""
#2 Write a Python program to print yesterday, today, tomorrow.
"""from datetime import datetime, timedelta
x = datetime.now()
print('Yesterday:', end = ' ')
print(x.strftime('%B'), end = " ") # month
y = datetime.now() - timedelta(days = 1) # you can't subtract timedelta from .strftime()
print(y.strftime('%d')) # print only day (without hours, ect.)
print('Today:', end = ' ')
print(x.strftime('%B'), end = " ") # month
print(x.strftime('%d')) # print only day (without hours, ect.)
print('Tomorrow:', end = ' ')
print(x.strftime('%B'), end = " ") # month
z = datetime.now() + timedelta(days = 1) # you can't subtract timedelta from .strftime()
print(z.strftime('%d')) # print only day (without hours, ect.)
"""
#3 Write a Python program to drop microseconds from datetime.
"""import datetime
x = datetime.datetime.now().replace(microsecond=0)
print(x)
"""
#4 Write a Python program to calculate two date difference in seconds.
"""from datetime import datetime, timedelta
dt1 = datetime.now()
dt2 = datetime.strptime('2023-02-17 00:00:00', '%Y-%m-%d %H:%M:%S')
timedelta = dt1 - dt2     #finds differents in days, hrs, seconds, microseconds
dif_sec = timedelta.days*24*3600 + timedelta.seconds
print(dif_sec)
"""
