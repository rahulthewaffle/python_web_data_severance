# prompt for a location
# contact a web service
# retrieve JSON for the web service
# parse that data
# retrieve the first place_id from the JSON

# API endpoint: http://py4e-data.dr-chuck.net/geojson?

import urllib.request as req, urllib.parse as parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location: ')

url = serviceurl + parse.urlencode({'address': address})

print('Retrieving', url)
data = req.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK' :
    print('Failure to retrieve requested address')
    print('data')
    raise SystemExit()
# else : print(json.dumps(js, indent = '\t'))

place_id = js['results'][0]['place_id']

print('Place id', place_id)
