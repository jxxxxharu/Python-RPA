"""import selenium"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv


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


"""무한 스크롤"""
before_h = browser.execute_script('return window.scrollY')  # 스크롤 전 높이

while True:
    browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)  # 맨 아래로 스크롤을 내린다.
    time.sleep(1)  # 스크롤 사이 페이지 로딩 시간
    
    after_h = browser.execute_script('return window.scrollY')  # 스크롤 후 높이
    if after_h == before_h: 
        break
    before_h = after_h
    
    
"""상품정보 div & csv 파일 저장"""
items = browser.find_elements(By.CSS_SELECTOR, '.basicList_info_area__17Xyo')

with open(r'C:\Users\yang9\Python-RPA\data.csv', 'w', encoding='cp949', newline='') as f:
    csvWriter = csv.writer(f)
    
    for item in items:
        name = item.find_element(By.CSS_SELECTOR, '.basicList_title__3P9Q7').text
        try:
            price = item.find_element(By.CSS_SELECTOR, '.price_num__2WUXn').text
        except:
            price = '판매중단'
        link = item.find_element(By.CSS_SELECTOR, '.basicList_title__3P9Q7 > a').get_attribute('href')
        
        print(name, price, link)
        csvWriter.writerow([name, price, link])  # 파일에 데이터 쓰기