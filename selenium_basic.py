"""import selenium"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


"""브라우저 생성"""
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 에러메세지 없애기
browser = webdriver.Chrome('C:/chromedriver.exe', options=options)  # chromedriver 버전 충돌 주의


"""웹 사이트 열기"""
url = 'https://www.naver.com'
browser.get(url)
browser.implicitly_wait(10)  # 로딩이 끝날 때까지 10초까지 기다림


"""쇼핑 메뉴 클릭"""
browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click()
time.sleep(2)


"""검색창 클릭"""
search = browser.find_element(By.CSS_SELECTOR, 'input._searchInput_search_input_QXUFf')
search.click()


"""검색창 입력"""
search.send_keys('바디로션')
search.send_keys(Keys.ENTER)