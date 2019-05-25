import urllib.request, urllib.parse, urllib.error
import json
import ssl


serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
#serviceurl= 'http://py4e-data.dr-chuck.net/json?'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#api_key=42

address = input('Enter location: ')
if len(address) < 1:
    exit()
parms = dict()
parms['address'] = address
parms['key']=api_key

url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')
try:
    js = json.loads(data)
    #print(type(js))
except:
    js = None

if js['status']=='OK':
    print(json.dumps(js,indent=4))
else:
    print('==== Failure To Retrieve ====')
    print(data)

lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)
