# this program checks if the given year is a leap year

year=int(input("Enter the year that you want to check : "))

isLeap = False
if (year%4 == 0):
    isLeap = True
    if year%100 == 0:
        isLeap = False
        if year%400 == 0:
            isLeap = True

if(isLeap):
    print("The year you entered is a leap year")
else:
    print("The year you entered is not a leap year")