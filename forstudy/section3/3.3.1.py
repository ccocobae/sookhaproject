import requests
import json

#r = requests.get('https://api.github.com/events')
#r.raise_for_status()
#print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'kim', domain='httpbin.org', path='/cookies')

#r = requests.get('http://httpbin.org/cookies', cookies=jar)
#r.raise_for_status()
#print(r.text)

#r = requests.get('https://github.com', timeout=3)
#print(r.text)

#r = requests.post('http://httpbin.org/post', data={'name':'kim'}, cookies=jar)
#print(r.text)

payload1 = {'key1':'value1', 'key2':'value2'}
payload2 = {'status':'hungry'}

r = requests.post('http://httpbin.org/post', data=payload1)  # form
r = requests.post('http://httpbin.org/post', data=json.dumps(payload1))  # json
