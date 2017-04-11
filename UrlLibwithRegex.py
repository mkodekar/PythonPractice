from urllib import request as req
from urllib import parse as p
import re as r

# simple post request
try:
    url = 'https://pythonprogramming.net/search'
    value = {'q': 'basic'}
    data = p.urlencode(value)
    datas = data.encode('utf-8')
    request = req.Request(url, datas)
    resp = req.urlopen(request)
    # print(resp.read())
    paragraphs = r.findall(r'<p>(.*?)</p>', str(resp.read()))
    for eachP in paragraphs:
        print(eachP)

except Exception as e:
    print(e)