from bs4 import BeautifulSoup
import requests

url = 'https://finance.naver.com/sise/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

popularItem = soup.select('ul.lst_pop > li > a')  # 기억해야 할 코드

i = 1

for item in popularItem:
    print(i, item.string)
    i += 1