# pip install selenium
# pip install bs4
# pip install requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/chromedriver.exe"
driver = webdriver.Chrome(path)

try:
    driver.get("http://www.kyobobook.co.kr/index.laf?OV_REFFER=https://www.google.com/")
    time.sleep(1)

    searchIndex = "파이썬" #검색어입력
    element = driver.find_element_by_class_name("main_input")
    element.send_keys(searchIndex) #값 넘겨줌
    driver.find_element_by_class_name("btn_search").click() #검색

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    pages = (bs.find("span", id = "totalpage").text)
    print(pages) #다하면 너무 많으니까 페이지 수 확인 후

    title = []
    for i in range(3):  #3페이지만
        time.sleep(1)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser") #파싱

        conts = bs.find("div", class_ = "list_search_result").find_all("td", class_="detail")
        title.append("page" + str(i+1))
        for c in conts :
            title.append(c.find("div", class_ = "title").find("strong").text)

        driver.find_element_by_xpath('//*[@id="contents_section"]/div[9]/div[1]/a[3]').click()


finally:
    for t in title:
        if t.find("page") != -1:
            print()
            print(t)
        else :
            print(t)
    driver.quit()
