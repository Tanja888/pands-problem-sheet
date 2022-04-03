
# Weekly Task 03 - Inputs string and outputs every second letter in reverse order
# Author: Tanja Juric

sentence = input ("Hi. Please enter any sentence: ")
sliced = sentence [:: -2]
print ("Every second letter of your sentence in reversed order is: " + sliced)

# ::-2 stands for [Start: Stop: Step] first ':' is where will the slicing start, second ':' where it will end and '-2' how it will jump