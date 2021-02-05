import requests # 웹 페이지 소스를 얻기 위한 패키지(기본 내장 패키지이다.)
from bs4 import BeautifulSoup # 웹 페이지 소스를 얻기 위한 패키지, 더 간단히 얻을 수 있다는 장점이 있다고 한다.
from datetime import datetime                                # (!pip install beautifulsoup4 으로 다운받을 수 있다.)
#import pandas as pd # 데이터를 처리하기 위한 가장 기본적인 패키지
import time # 사이트를 불러올 때, 작업 지연시간을 지정해주기 위한 패키지이다. (사이트가 늦게 켜지면 에러가 발생하기 때문)
import urllib.request #
from selenium import webdriver
import json
import re     
import datetime as dt

def ttt(xx):
    name = xx
    base_url = 'https://finance.naver.com/item/coinfo.nhn?code='+ name + '&target=finsum_more'
    return base_url
    

browser = webdriver.Chrome("/Users/yoonseonghyeon/Desktop/programming/python/selenium/chromedriver")
browser.maximize_window()

browser.get(ttt('066571'))

browser.switch_to_frame(browser.find_element_by_id('coinfo_cp')) #frame구조 안으로 들어가기