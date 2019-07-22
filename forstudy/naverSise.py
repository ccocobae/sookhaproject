from bs4 import BeautifulSoup
import urllib.request as req

url = 'https://finance.naver.com/sise/'
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')

top5 = soup.select('#siselist_tab_0 > tr')  # 기억해야 할 코드

i = 1
for e in top5:
    if e.find('a') is not None :
        print(i, e.select_one(".tltle").string)
        i += 1