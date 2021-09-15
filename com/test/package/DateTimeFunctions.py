import datetime as dt
print(dt.date.today())

new = dt.date(2021,10,25)
print(new)

print("Year: ", new.year)
print("Month: ", new.month)
print("Day: ", new.day)

#```````````````````````````````````````````````````````````````````

print(dt.datetime.now().time())
#print(dt.time.strftime("%H:%M:%S", dt.datetime.now().time()))
a = dt.time(10,45,5,555505)
print(a)
print(a.hour) # similarly we can get other values


# finding date diff

curent = dt.datetime.now()
newyear = dt.datetime(2022,1,1)
diff = newyear - curent
print(diff)

# printing date time in specific format

current = dt.datetime.now()
print(current)
s = current.strftime("%A %B %d %Y")

'''
https://www.w3schools.com/python/python_datetime.asp
check this url for deciding the pattern in ehi
'''






























