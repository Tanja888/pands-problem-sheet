# Weekly task 05 - Wether or not today is a weekday
# Author: Tanja Juric

# I took the function from here: 
# URL: https://stackoverflow.com/questions/8380389/how-to-get-day-name-from-datetime
# The result is good - it shows the correct day
# %A shows full week day name, URL: https://www.programiz.com/python-programming/datetime/strptime

import datetime

now = datetime.datetime.now() 
day = now.strftime("%A")
print (day)
#strftime() converts date and time objects to their string representation

if day == "Saturday" or day == "Sunday":
    print ("Yay, today is weekend!")

else:
    print ("Unfortunately, today is a working day.")
