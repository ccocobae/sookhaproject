import requests
import json

s = requests.Session()
r = s.get('http://httpbin.org/stream/20', stream=True)
print(r.text)
print(r.encoding)

if r.encoding is None :
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    b = json.loads(line)  # dictionary 형식
    #  print(b['origin'])
    for e in b.keys():
        print("key :", e, ", value :", b[e])