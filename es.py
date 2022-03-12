# Weekly Task 07
# Reads in a text file and outputs the number of e's it contains
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

# Couldn't read in a text file so I added encodinf="utf-8", found it here:
# URL: https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
# URL of the article for the text file: https://www.washingtonpost.com/world/2022/03/09/letter-z-russia-symbol-pro-war/
# Here I checked how to get the frequency URL: https://stackoverflow.com/questions/22694244/counting-specific-letters-or-symbols-in-a-text-file-in-python

# From the same URL, shorter way of calculating the frequency:

with open ("warSymbol.txt", "rt", encoding="utf-8") as f:
    data = f.read()
    freq = data.count('e')
    print(freq)

