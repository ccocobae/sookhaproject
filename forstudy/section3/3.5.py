from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

# Wishket 크롤링
# 필요한 정보 : csrf token 과 headers 의 user agent, referer(바로 전에 어느 사이트에 있었는지에 대한 정보)
URL = 'https://www.wishket.com/accounts/login/'

ua = UserAgent()

with requests.Session() as s:
    # 요청하기 전 URL 연결 -> 접속이 이루어지면서 csrf 토큰 쿠키가 생김
    s.get(URL)
    # Login 정보 Payload
    LOGIN_INFO = {
        'identification': 'kaithape',
        'password': 'password',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }

    # 요청
    response = s.post(URL, data=LOGIN_INFO, headers={'User-Agent': str(ua.chrome), 'Referer': "https://www.wishket.com/accounts/login/"})
    # HTML 결과 확인
    # print('response', response.text)
    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        projectList = soup.select('table.table-responsive > tbody > tr')
        for i in projectList:
            print(i.get_text())
            # td, tr 태그를 각각 find() 해서 따로 출력하는 것도 가능
