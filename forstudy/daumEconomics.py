import urllib.request as req
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import sys
import io

ua = UserAgent()

headers = {
    'User-Agent': ua.ie,
    'referer': 'https://finance.daum.net/'
}

url = "https://finance.daum.net/api/search/ranks?limit=10"

res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

rank_json = json.loads(res)['data']

print('중간 확인 :', rank_json, '\n')

for elm in rank_json:
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm['tradePrice'], elm['name']), )

