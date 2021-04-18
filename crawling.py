from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome(
    "/Users/yoonseonghyeon/Desktop/programming/python/selenium/chromedriver")
driver.get("https://unsplash.com/backgrounds/phone")


SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

imgUrls = []
count = 0
while count < 5:
    count += 1
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    last_height = new_height

#imgs = driver.find_elements_by_css_selector("._3UDio")

while True:
    try:
        time.sleep(0.1)
        imgUrl = driver.find_element_by_css_selector(
            "._2UpQX").get_attribute("src")
        # imgUrl = driver.find_element_by_xpath("/html/body/div/div/div[4]/div[1]/div/div/div["+str(i)+"]/div["+str(count)+"]/figure/div/div[1]/div/div/a/div/div[2]/div/img").get_attribute("src")
        imgUrls.append(imgUrl)
        print(imgUrl)
    except:
        break

print(imgUrls)

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
