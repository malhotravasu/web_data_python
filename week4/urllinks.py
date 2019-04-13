import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
relative_pos = int(input('Enter Relative Position: '))-1
total_iters = int(input('Enter Total Redirects: '))

names = []
for _ in range(total_iters):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    tag = tags[relative_pos]
    names.append(tag.contents[0])
    url = tag.get('href', None)

print(names[-1])