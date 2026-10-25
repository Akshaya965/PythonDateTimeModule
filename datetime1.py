from datetime import date,  datetime

#calling the today
#function of the date class
today = date.today()
now = datetime.now()
print("Today's date is:", today)
print("\nCurrent Date and time is ", now)

print("\nDate components", today.year, today.month, today.day)