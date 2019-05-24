from urllib.request import urlopen

import json
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location : ')
print('Retrieving ',url)
html = urlopen(url, context=ctx).read()
print('Retrieved',len(html.decode()),'characters')

tree= ET.fromstring(html.decode())
c=0
s=0

lst = tree.findall('comments/comment/count')
print('Count: ',len(lst))
s=0
for c in lst:
    s=s+int(c.text)
print('Sum: ',s)
