#DemoForm2.py
#DemoForm2.ui(화면단)+ DemoForm2.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests
from bs4 import BeautifulSoup

form_class = uic.loadUiType("DemoForm2.ui")[0]

class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면 출력")
    #슬롯 메소드
    def firstClick(self):
        url="https://www.daangn.com/fleamarket/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'html.parser')
        #상단의 <div>태그 검색
        f=open("daangn.txt","wt",encoding="utf-8")
        posts = soup.find_all('div',attrs={'class':'card-desc'})
        for post in posts:
            titleElem = post.find('h2',attrs={'class':'card-title'})
            priceElem = post.find('div',attrs={'class':'card-price'})
            regionElem = post.find('div',attrs={'class':'card-region-name'})
            title = titleElem.text.strip()
            price=priceElem.text.strip()
            region=regionElem.text.strip()
            print(f"{title},{price},{region}")
            f.write(f"{title},{price},{region}\n")
        f.close()
        self.label.setText("당근마켓 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭")
#진입점 체크: c언어 main()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
