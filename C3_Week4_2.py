import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL : ')
count=int(input('Enter count : '))
pos=int(input('Enter position : '))

for i in range(count+1):
    print('Retrieving: ',url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    c=0
    for tag in tags:
        c=c+1
        if c==pos:
          url=tag.get('href', None)
