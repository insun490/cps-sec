from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/chromedriver.exe"
driver = webdriver.Chrome(path)

# 지니에서 정승환 노래 제목 추출 

try:
    driver.get("https://www.genie.co.kr/")
    time.sleep(1)

    searchIndex = "정승환" #검색어입력
    element = driver.find_element_by_xpath('//*[@id="sc-fd"]')
    element.send_keys(searchIndex) #값 넘겨줌
    driver.find_element_by_xpath('//*[@id="frmGNB"]/fieldset/input[3]').click() #검색
    driver.find_element_by_xpath('//*[@id="body-content"]/div[2]/ul/li[3]/a').click() #통함검색에서 곡 파트로 이동

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    title = []
    for i in range(3):  #3페이지만
        time.sleep(1)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser") #파싱

        conts = bs.find_all("td", class_="info")
        for c in conts :
            title.append(c.find("a", class_ = "title ellipsis").text) #곡 제목 담기

        driver.find_element_by_xpath('//*[@id="body-content"]/div[4]/div[5]/a[13]').click() #다음페이지 


finally:
    print(title)
    time.sleep(1)
    driver.quit()
