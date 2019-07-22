import requests
import json



jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'kim', domain='httpbin.org', path='/cookies')

payload1 = {'key1':'value1', 'key2':'value2'}
payload2 = {'status':'hungry'}

r = requests.post('http://httpbin.org/post', data=payload1)  # form
r = requests.post('http://httpbin.org/post', data=json.dumps(payload1))  # json
