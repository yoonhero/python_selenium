from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
종목 = str(input("종목을 선택해 주세요:  "))
driver = webdriver.Chrome("/Users/yoonseonghyeon/Desktop/programming/python/selenium/chromedriver")
driver.get("https://finance.naver.com/")
inputElement = driver.find_element_by_id("stock_items")
inputElement.send_keys(종목)
inputElement.send_keys(Keys.RETURN)
try:
    p = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[4]/table/tbody/tr[1]/td[2]').text
    print(p)
except:
    pass
time.sleep(3)

driver.close()

