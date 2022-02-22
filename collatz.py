# Weekly Task 04 - Collatz 
# Author: Tanja Juric

number = int(input("Please enter a positive integer: "))

# Variable number has to be different than 1 to enter the while loop
# If number is 1 the program will end
while number != 1:   

# if the number is even divide it by 2
# introduced the variable result because that will represent the changed variable 'number' which is being checked in the condition of the while
    if number % 2 == 0: 
        result = int(number / 2)
    else: 
        result = (number * 3) + 1

    print(result)
    number = result
print ("The End") # when the result reached False (= 1) print 'The End' because the loop ended
