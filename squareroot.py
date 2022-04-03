# Weekly Task 06 - Creating a square root function 
# Author: Tanja Juric

# I had difficulties with this task, I didn't really get it but found the solution.

x = float(input("Please enter a positive number: "))

def mySqrt(x):
    r = x
    precision = 10 ** (-10) #This is the level of precision, very small number

    while abs(x - r * r) > precision:
        r = (r + x / r) / 2
    
    return r 

print("The square root of {} is approx. {}." .format(x, round(mySqrt(x),1)))