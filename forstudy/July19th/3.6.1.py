from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#  chrome_options = Options()
#  chrome_options.add_argument("--headless")  # command line interface 설정

driver = webdriver.Chrome('/Users/soo/PycharmProjects/crawling/driver/chrome/chromedriver')
#  driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/Users/soo/PycharmProjects/crawling/driver/chrome/chromedriver')

driver.get('https://google.com')
driver.save_screenshot('/Users/soo/PycharmProjects/crawling/screenshot_ch1.png')

driver.get('https://www.daum.net')
driver.save_screenshot('/Users/soo/PycharmProjects/crawling/screenshot_ch2.png')

driver.quit()

print("스크린샷 완료!")

# 브라우저로 직접 제어하기 때문에 fake user-agent 를 사용하거나 cookie를 털 필요가 없음