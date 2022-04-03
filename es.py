# Weekly Task 07 - Reads in a text file and outputs the number of e's it contains
# Author: Tanja Juric

# Take the filename from an argument on the command line - didn't check this yet, wanted to count the e's first

filename = 'warSymbol.txt'
with open(filename, 'rt', encoding="utf-8") as f:
   data = f.read()
   #print(data)
   freq = 0
   for char in data:
       if char == 'e':
           freq = freq + 1
print(freq)

# From the same URL, shorter way of calculating the frequency:

with open ("warSymbol.txt", "rt", encoding="utf-8") as f:
    data = f.read()
    freq = data.count('e')
    print(freq)

