
# Weekly Task 03 - Inputs string and outputs every second letter in reverse order
# Author: Tanja Juric

sentence = input ("Hi. Please enter any sentence: ")
sliced = sentence [:: -2]
print ("Every second letter of your sentence in reversed order is: " + sliced)


# Still not sure where to put references, I have to check videos on how to make a RADME nice
# First I searched how to reverse the string; URL: https://www.w3schools.com/python/python_howto_reverse_string.asp
# Then I was wondering what is slicing; URL: https://www.w3schools.com/python/ref_func_slice.asp
# I also didn't understand what does double colon stand for; URL: https://www.askpython.com/python/examples/colon-in-python
# ::-2 stands for [Start: Stop: Step] first ':' is where will the slicing start, second ':' where it will end and '-2' how will it jump