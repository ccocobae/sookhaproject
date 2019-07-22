from bs4 import BeautifulSoup
import requests

# 로그인 유저정보, form 형식으로 전달
LOGIN_INFO = {
    'user_id': 'kaithape',
    'user_pw': 'password'
}

# Session 설정, with 구문 안에서 유지
with requests.Session() as s:
    # post()로 루리웹에 내 로그인 정보 전달. 이 코드 주석처리하면 "권한이 없거나 로그인이 필요합니다"가 출력됨
    login_req = s.post('https://user.ruliweb.com/member/login_proc', data=LOGIN_INFO)
    # Html 소스 확인
    # print('login_req', login_req.text)
    # Header 확인
    # print('headers', login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('https://market.ruliweb.com/read.htm?table=market_ngc&num=551854')
        post_one.raise_for_status() # 200   OK 코드가 아닌 경우 에러 발
        soup = BeautifulSoup(post_one.text, 'html.parser')
        # print(soup.prettify())
        # 본문 내용만 가져오기
        article = soup.find_all('td', 'con')[2]
        for i in article.find_all('p'):
            if i.string is not None:
                print(i.string.strip())