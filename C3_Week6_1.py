from urllib.request import urlopen
import json
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter location : ')
print('Retrieving ',url)
html = urlopen(url, context=ctx).read()
print('Retrieved',len(html.decode()),'characters')
      

x=json.loads(html.decode())

l_comm=x['comments']


c=0
s=0
for comm in l_comm:
    c=c+1
    s=s+comm['count']

print('Count:',c)
print('Sum:',s)
