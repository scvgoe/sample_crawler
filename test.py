from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import datetime

#driver = webdriver.PhantomJS('/usr/local/bin/phantomjs')
driver = webdriver.Chrome('/Users/daesungkim/Downloads/chromedriver')

def frame_available_cb(frame_reference):
    """Return a callback that checks whether the frame is available."""
    def callback(browser):
        try:
            browser.switch_to_frame(frame_reference)
        except NoSuchFrameException:
            return False
        else:
            return True
    return callback

def login(id, password):
    driver.get('https://login.aliexpress.com')
    try:
        WebDriverWait(driver, 3).until(frame_available_cb("alibaba-login-box"))
        driver.find_element_by_id('fm-login-id').send_keys(id)
        driver.find_element_by_id('fm-login-password').send_keys(password)
        driver.find_element_by_id('fm-login-submit').click()
        print("login success")
    except TimeoutException:
        print("Loading took too much time!")

def search(keyword):
    driver.get('https://aliexpress.com')

    search_form = driver.find_element_by_id('search-key')
    search_form.send_keys(keyword)
    search_form.submit()

    temp = True
    while (temp):
        try:
            cur = driver.find_element_by_css_selector(".ui-pagination-active")
            print(cur.text)
            link = driver.find_element_by_css_selector(".page-next.ui-pagination-next")
            link.click()
        except:
            temp = False

login('', '')
print(datetime.datetime.now())
sample_keyword = ['가방', '바지', '전구', '청소기', '시계', '신발']
for keyword in sample_keyword:
    print(keyword)
    search(keyword)
print(datetime.datetime.now())
