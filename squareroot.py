# Creating a square root function 
# Author: Tanja Juric

# I need to check the Newton method

# I had difficulties with this task, I didn't really get it but here is the solution I found here:
# URL https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo

x = float(input("Please enter a positive number: "))

def mySqrt(x):
    r = x
    precision = 10 ** (-10) #This is the level of precision, very small number

    while abs(x - r * r) > precision:
        r = (r + x / r) / 2
    
    return r 

print("The square root of {} is approx. {}." .format(x, round(mySqrt(x),1)))