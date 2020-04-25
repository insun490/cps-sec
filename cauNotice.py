from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time #위 2개는 내장모듈. 별도 설치 필요 없음.

path = os.getcwd() + "/chromedriver.exe"

driver = webdriver.Chrome(path)

try : #try밑에 있는 코드들 실행.
    driver.get("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100&CONTENTS_NO=2&P_TAB_NO=2#page1")
    time.sleep(1) #컴퓨터 성능에 따라 시간 조절

    html = driver.page_source #requests.get().text
    bs = BeautifulSoup(html, "html.parser")

    pages = bs.find("div", class_="pagination").find_all("a")[-1]["href"].split("page")[1]
    pages = int(pages)
    
    title = [] #제목 저장할 부분
    for i in range(3):
        driver.get(("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100&CONTENTS_NO=2&P_TAB_NO=2#page") + str(i+1))
        time.sleep(3)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find_all("div", class_="txtL")
        title.append("page" + str(i+1))

        for c in conts :
            title.append(c.find("a").text)
    #find_all함수는 reture을 리스트로 함.

finally:
    #time.sleep(3)
    for t in title:
        if t.find("page"):
            print()
            print(t)
        else :
            print(t)
    driver.quit()

#time.sleep(3)

#driver.quit()
