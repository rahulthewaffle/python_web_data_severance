# prompt for a URL
# read the XML data from that URL using urllib
# parse and extract the comment counts from the XML data
# compute the sum of the numbers in the file

# sample url: http://py4e-data.dr-chuck.net/comments_42.xml
# test url: http://py4e-data.dr-chuck.net/comments_18186.xml

import urllib.request as req, urllib.parse as parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)

data = req.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Count:', len(counts))

sum = 0
for count in counts :
    sum += int(count.text)

print('Sum:', sum)
