import requests

s = requests.Session()
r = s.get('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)
print(r.json())  # 딕셔너리로 convert해서 보여줌


