from selenium import webdriver


chromedriver = ""  # chrominum 설치 경로를 입력해주세요
driver = webdriver.Chrome(chromedriver)


def getSiteName(sitename):  # 사이트 이름을 알아내는 함수
    driver.get(sitename)  # sitename 으로 전달된 값을 driver가 열기
    return driver.title  # 열은 브라우저의 title을 return


f = open("./site.txt", "r")  # site를 담은 site.txt

site_list = []  # 사이트를 담을 리스트 선언

while True:  # site.txt 한줄씩 읽어오기
    line = f.readline()
    if not line:
        break  # 값이 없으면 종료
    site_list.append(line)  # 읽은 값 추가

f.close()

for site in site_list:
    sitename = getSiteName(site)  # 함수 실행해 값을 변수로
    print(site, sitename)  # site이름과 title을 출력

driver.quit()
