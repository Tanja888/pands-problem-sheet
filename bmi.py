
# Weekly Task 02 - Calculating BMI
# Author: Tanja Juric

print ('Hello! Today we are going to calculate your Body Mass Index, known as BMI.')

height = int(input('Please enter your height in centimetres: ')) #not sure if float or int
weight = float(input('Please enter your weight in kilograms: ')) #not sure if float or int

heightInMeters = height/100
powerOfMeters = heightInMeters ** 2

# BMI is kg/m2 - need to figure out how the write a superscript here
bmi = weight / powerOfMeters
bmi = round(bmi, 2)
print ('Your BMI is: {}' .format(bmi))

# Another way of calculating
bmi = weight / (heightInMeters * heightInMeters)
bmi = round(bmi, 2)
print ('Your BMI is: {}' .format(bmi))
print ('Your BMI is ' + str(bmi))


# not sure where to put references
# URL: https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792
# URL: https://www.codegrepper.com/code-examples/python/how+to+round+with+format+in+python



