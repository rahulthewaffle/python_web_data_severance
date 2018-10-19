#find all the <span> tags in the file
#pull out the numbers from the tag
#sum the numbers

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')

numbers = list()

for tag in tags :
    temp = re.findall('[0-9]+', tag.contents[0])
    numbers.extend(temp)

sum = 0
count = len(numbers)

for number in numbers :
    sum += int(number)

print('Sum = ' + str(sum))
print('Count = ' + str(count))
