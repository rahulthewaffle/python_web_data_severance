# use urllib to read the HTML from the data files
# extract the href= vaues from the anchor tags
# scan for a tag that is in a particular position relative to the first name in the list
# follow that link and repeat the process a number of times
# report the last name you find

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
html = urllib.request.urlopen(url, context=ctx).read()

pos = int(input('Enter name position - '))
repeats = int(input('Enter number of repeats - '))

name = re.findall('by_([A-Za-z]+)\.h', url)
print('Retrieving: People Known By ' + name[0])

for i in range(0,repeats) :
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    j = 1
    for tag in tags:
        if(j == pos) :
            url = tag.get('href', None)
            name = re.findall('by_([A-Za-z]+)\.h', url)
            print('Retrieving: People Known By ' + name[0])
            break
        j+= 1

    if i < repeats :
        html = urllib.request.urlopen(url, context = ctx).read()
