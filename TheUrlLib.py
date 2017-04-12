from sys import stderr as serr
from urllib import parse as p
from urllib import request as r

# simple get request
x = r.urlopen('https://duckduckgo.com')
print(x.read())

# simple post request
url = 'https://pythonprogramming.net/search'
value = {'q': 'basic'}
data = p.urlencode(value)
data = data.encode('utf-8')
req = r.Request(url, data)
resp = r.urlopen(req)
print(resp.read())

# user agent 'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'

try:
    url = 'https://duckduckgo.com/?q=test'
    headers = {}
    headers['User-agent'] = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
    req = r.Request(url, headers=headers)
    resp = r.urlopen(req)
    respData = resp.read()

    saveFile = open('SearchResponse.html', 'w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    serr.write(e)
    serr.flush()
