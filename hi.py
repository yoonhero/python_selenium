def getSiteNameParameter(name):
    name.replace("'", '"')  # 작은 따옴표를 큰 따옴표로 변환
    if "name=" in name:  # name 인자에 "name=" 글자가 있다면
        i = name.index("name=")  # name= 의 인덱스 구하기
        count = 0
        indexs = []
        for a in range(i+5, len(name)):  # name= 이후에 " 찾기
            text = name[a]
            if count >= 2:  # 큰따옴표를 두 번 찾아으니 반복문 종료
                break
            if text == '"':
                indexs.append(a)
                count += 1

        return name[indexs[0]+1:indexs[1]]


f = open("./site.txt", "r")  # site를 담은 site.txt

site_list = []  # 사이트를 담을 리스트 선언

while True:  # site.txt 한줄씩 읽어오기
    line = f.readline()
    if not line:
        break  # 값이 없으면 종료
    site_list.append(line)  # 읽은 값 추가

for site in site_list:
    sitename = getSiteNameParameter(site)  # 함수 실행해 값을 변수로
    print(site, sitename)  # site이름과 title을 출력


f.close()
