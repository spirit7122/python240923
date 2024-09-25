#web2.py
import requests
from bs4 import BeautifulSoup
#    <div class="card-desc">
#       <h2 class="card-title">아이폰 14 128GB</h2>
#       <div class="card-price ">
#         600,000원
#       </div>
#       <div class="card-
# -name">
#         전남 순천시 용당동
#       </div>

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

