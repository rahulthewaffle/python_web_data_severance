import re

fname = input("Enter file name: ")
fh = open(fname)

sum = 0

for line in fh :
    numbers = re.findall('[0-9]+', line)
    for value in numbers :
        sum += int(value)

print(sum)
