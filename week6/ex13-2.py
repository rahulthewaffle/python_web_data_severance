# prompt for a URL
# read the JSON data from that URL using urllib
# parse and extract the comment counts from the JSON data
# compute the sum of the numbers in the file

# sample url: http://py4e-data.dr-chuck.net/comments_42.json
# test url: http://py4e-data.dr-chuck.net/comments_18187.json

import json
import urllib.request as req, urllib.parse as parse, urllib.error

url = input('Enter location: ')
print('Retrieving', url)

data = req.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
comments = js['comments']
print('Count:', len(comments))

sum = 0
for comment in comments :
    sum += comment['count']

print('Sum:', sum)
