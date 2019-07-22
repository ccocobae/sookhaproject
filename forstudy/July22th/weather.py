import urllib.request as req
from bs4 import BeautifulSoup
import os.path

# xml 또한 BeautifulSoup 로 파싱이 가능하다!

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3017055500"
savename = "/Users/soo/PycharmProjects/crawling/July22th/forecast.xml"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

xml = open(savename, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')  # xml 은 html 의 성격을 가지기 때문

date = 23
print("7월 22일")
for datum in soup.find_all("data"):
    hour = datum.find("hour")
    weather = datum.find("wfkor")

    if hour.string == str(3):
        print("\n7월 %d일" % date)
        date += 1

    print(hour.string + "시 " + weather.string)