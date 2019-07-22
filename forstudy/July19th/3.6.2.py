from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class NcafeWriteAtt:
    # 초기화 실행(webdriver 설정)
    def __init__(self):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/Users/soo/PycharmProjects/crawling/driver/chrome/chromedriver')
        self.driver = webdriver.Chrome('/Users/soo/PycharmProjects/crawling/driver/chrome/chromedriver')
        self.driver.implicitly_wait(5)

        # 네이버 카페 로그인 및 출석 체크
    def writeAttendCheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('suyohnee')
        self.driver.find_element_by_name('pw').send_keys('password')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(30)
        self.driver.get('https://cafe.naver.com/AttendanceView.nhn?search.clubid=25997591&search.menuid=56')
        self.driver.implicitly_wait(10)
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_id('cmtinput').send_keys('출석합니다')
        self.driver.find_element_by_xpath('//*[@id="btn-submit-attendance"]').click()
        time.sleep(3)


if __name__ == '__main__':
    a = NcafeWriteAtt()
    start_time = time.time()
    a.writeAttendCheck()
    end_time = time.time()

    print("------ Total %s seconds ------" %(end_time - start_time))

