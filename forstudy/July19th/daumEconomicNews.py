import requests
from bs4 import BeautifulSoup

res = requests.get('https://media.daum.net/economic/')
soup = BeautifulSoup(res.content, 'html.parser')

links = soup.select('a[href]')  # a 태그 중에서 href 속성을 가지고 있는 코드를 select

for link in links:
    print(link['href'])