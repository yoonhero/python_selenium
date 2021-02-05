import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code="


for i in range(1, 100):
    n = 6 - len(str(i)) # 몇 자리수 인가?
    stock_num = "0" * n + str(i) #종목명

    # print(stock_num)


    res = requests.get(url + str(stock_num))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"tb_type1_ifrs"}).find("tbody").find_all("tr")
    print(data_rows)


