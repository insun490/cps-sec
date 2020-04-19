import requests
from bs4 import BeautifulSoup
import csv

#텐바이텐 베스트셀러 크롤링

class BestScraper :

    def __init__(self) : 
        self.url = "http://www.10x10.co.kr/award/awardlist.asp?atype=b&gaparam=main_menu_best"

# 웹 사이트에서 HTML 받아오기

    def getHTML(self) :
        res = requests.get(self.url)
        if res.status_code != 200 :
            print("bad request", res.status_code)
        html = res.text
        soup = BeautifulSoup(html, "html.parser")
        return soup

# 내용 받아오기(판매업체, 판매물품, 가격)

    def getContent(self, soup):

        seller = []
        things = []
        price = []

        soup = self.getHTML()
        box = soup.find_all("li", class_ = "bestUpV15")

        for b in box:
            if b.find("p", class_="pdtBrand tPad20") != None :
                seller.append(b.find("p", class_="pdtBrand tPad20").text)
            if b.find("p", class_="pdtName tPad07") != None :
                things.append(b.find("p", class_="pdtName tPad07").text)
            if b.find("p", class_="pdtPrice") != None :
                price.append(b.find("span", class_="finalP").text)
        
        self.writeCSV(seller, things, price)


# CSV 입력 함수
    def writeCSV(self, seller, things, price):
        file = open("크롤링.csv", "a", newline="", encoding = 'UTF8')
        wr = csv.writer(file)
        for i in range(len(seller)):
            wr.writerow([seller[i], things[i], price[i]])
        file.close

# scrap 함수
    def scrap(self) :

        file = open("크롤링.csv", "w", newline="", encoding='UTF8')
        wr = csv.writer(file)
        wr.writerow(["판매업체", "판매물품", "가격"])
        file.close()

        self.getContent(self)

if __name__== "__main__" :
    s = BestScraper()
    s.scrap()