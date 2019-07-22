from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os

opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
quote = rep.quote_plus("고양이")  # 검색어 입력
url = base + quote

res = req.urlopen(url)
savePath = "soo/imagedownload/"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e :
    print(e)

soup = BeautifulSoup(res, 'html.parser')

img_list = soup.find_all('img', '_img')

for i, img_list in enumerate(img_list,1):
    fullFileName = os.path.join(savePath, str(i)+'.jpg')
    req.urlretrieve(img_list['data-source'], fullFileName)

print("다운로드 완료")