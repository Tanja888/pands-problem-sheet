# Weekly task 05 - Wether or not today is a weekday
# Author: Tanja Juric

# I don't get yet what I did - took it from here: 
# URL: https://stackoverflow.com/questions/8380389/how-to-get-day-name-from-datetime
# The result is good - it shows the correct day
# %A shows full week day name, URL: https://www.programiz.com/python-programming/datetime/strptime

import datetime

now = datetime.datetime.now() 
print (now.strftime("%A")) #strftime() converts date and time objects to their string representation

# now I need to separate working days from weekend and include 'now' somehow