from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

url = 'https://www.inflearn.com/courses/it-programming?skill=python&order=seq'

res = req.urlopen(url)
savePath = "soo/imagedownload/"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e :
    print(e)

soup = BeautifulSoup(res, 'html.parser')

title = soup.find_all('div', 'course_title')
for i in title :
    tl = i.get_text().strip()
    print(tl, type(tl))

img_list = soup.select('div.card-image')

j = 0
for i, img_list in enumerate(img_list, 1):
    with open(savePath+"text_"+str(i)+'.txt', 'wt') as f:
        tl = title[j].get_text()
        f.write(tl.strip())
    fullFileName = os.path.join(savePath, str(title[j].get_text().strip()) + ".png")
    j += 1
    req.urlretrieve(img_list.select_one('figure.image.is_thumbnail > img')['src'], fullFileName)

print("다운로드 완료")
