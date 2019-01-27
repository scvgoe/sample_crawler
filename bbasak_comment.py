from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import datetime
from time import sleep

driver = webdriver.Chrome('/Users/daesungkim/Downloads/chromedriver')

def login_to_bbasak(id, pw):
    driver.get('https://bbasak.com/bbs/login.php')
    try:
        driver.find_element_by_id('login_id').send_keys(id)
        driver.find_element_by_id('login_pw').send_keys(pw)
        driver.find_element_by_class_name('login-btn').click()
        print("login success")
    except TimeoutException:
        print("Loading took too much time!")

def comment_to_bbasak(content):
    try:
        driver.find_element_by_id('wr_content').send_keys(content)
        driver.find_element_by_id('comment_write').find_element_by_class_name('cmt_btn').click()
    except TimeoutException:
        print("Loading took too much time!")

login_to_bbasak()
driver.get('http://bbasak.com/bbs/board.php?bo_table=com1&wr_id=1090001')
for i in range(100):
    comment_to_bbasak()
    next_url = driver.find_element_by_id('board_href_move').find_elements_by_tag_name('a')[1].get_attribute('href')
    driver.get(next_url)
    sleep(3)
