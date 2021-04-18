from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


driver = webdriver.Chrome(
    "/Users/yoonseonghyeon/Desktop/programming/python/selenium/chromedriver")

i = 0

while i < 1000:
    driver.switch_to.window(driver.window_handles[0])
    i += 1
    driver.get("https://hardtosay.netlify.app/")
    add = driver.find_element_by_css_selector(".kakao_ad_area")
    add.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.close()

driver.quit()
