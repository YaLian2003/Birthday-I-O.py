Yangyang Lian
07/02/2023
CS 10 Birthday

def isLeapYear(year):
return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

def getMaxDays(month, year):
daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (isLeapYear(year) and month == 2):
return daysInMonths[month - 1] + 1
else :
return daysInMonths[month - 1]

def isValidDate(month, year, day):
if (month < 1 or month > 12):
return False
else:
maxDays = getMaxDays(month, year);
return not (day < 1 or day > maxDays);

def readADate(prompt):
m = int(input('Enter the birth month of Person ' + prompt + ': '))
d = int(input('Enter the birth day of Person ' + prompt + ': '))
y = int(input('Enter the birth year of Person ' + prompt + ': '))
print()
return (d, y, m)
print()

Day=(Date + Month + calcYear) % 7
print("The date is %d"%Date)
print("The month is %d"%Month)
print("The calculated year is %d"%calcYear)
print("The code for day is %d"%Day) 

if Day in [0]:
    print("You were born on a Sunday")
elif Day in [1]:
    print("You were born on a Monday")
elif Day in [2]:
    print("You were born on a Tuesday")
elif Day in [3]:
    print("You were born on a Wednesday")
elif Day in [4]:
    print("You were born on a Thursday")
elif Day in [5]:
    print("You were born on a Friday")
elif Day in [6]:
    print("You were born on a Saturday")
