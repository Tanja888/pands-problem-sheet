# Weekly task 05 - Wether or not today is a weekday
# Author: Tanja Juric

import datetime

now = datetime.datetime.now() 
day = now.strftime("%A")
print (day)
#strftime() converts date and time objects to their string representation

if day == "Saturday" or day == "Sunday":
    print ("Yay, today is weekend!")

else:
    print ("Unfortunately, today is a working day.")

