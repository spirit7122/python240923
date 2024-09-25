#크롤링 선언
from bs4 import BeautifulSoup

with open("Chap09_test.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())
#문서에 있는 p태그찾기
# print(soup.find_all('p'))

#첫번째 p 태그
# print(soup.find('p'))
#조건에 맞는 p 태그
# print(soup.find_all('p',class_='outer-text'))
#최근에는 attrs속성 제공
# print(soup.find_all('p',attrs=('class':'outer-text')))

#찾은 결과를 루프돌리기
for p in soup.find_all('p'):
    title=p.text.strip()
    print(title)    

