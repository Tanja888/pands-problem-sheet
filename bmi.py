
# Weekly Task 02 - Calculating BMI
# Author: Tanja Juric

print ('Hello! Today we are going to calculate your Body Mass Index, known as BMI.')

height = float(input('Please enter your height in centimetres: ')) 
weight = float(input('Please enter your weight in kilograms: ')) 

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





