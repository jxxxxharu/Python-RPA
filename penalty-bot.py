from re import M
from turtle import done
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome('C:/chromedriver.exe', options=options)

browser.set_window_size(100, 900)
url = r'https://github.com/banana970/Let-s-do-study'
browser.get(url)

""" 'View code' 버튼 펼치기 """
unfold = browser.find_element(By.CSS_SELECTOR, '.Box-footer > button')
if unfold.get_attribute('aria-expanded') == 'false':
    unfold.click()

""" 해당 주차 폴더 클릭 """
WEEK = 'Summer_Week_5'  # 매주 입력값
browser.find_element(By.LINK_TEXT, WEEK).click()
time.sleep(0.5)

    
""" 문제 별로 제출한 사람 확인 """
MEMBERS = ['승주', '수경', '세민', '승수', '희오', '조은', '상민', '주혜', '혜온', '재열']  # 멤버 목록
NUMBER = len(MEMBERS)
problems = browser.find_elements(By.CSS_SELECTOR, '.Box-row--focus-gray .js-navigation-open')[1:]
# for p in problems:
problems[0].click()
done = []
submits = browser.find_elements(By.CSS_SELECTOR, '.Box-row--focus-gray .js-navigation-open')[1:]  # 왜 안 돼 지인짜...
for submit in submits:
    done = [member for member in MEMBERS if member in submit.text]  # 푼 사람
browser.back()