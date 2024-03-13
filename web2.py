# web2.py 
# 웹서버와 통신(요청)
import urllib.request

# 크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
page = urllib.request.urlopen(url).read()

# 검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")

# 파일로 저장
f = open("dangn.txt", "wt", encoding="utf-8")

# 필터링 작업
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.replace("\n","").strip()
    price = priceElem.text.replace("\n","").strip()
    addr = addrElem.text.replace("\n","").strip()
    print(f"{title} / {price} / {addr}")
    f.write(f"{title} / {price} / {addr}\n")

# 파일쓰기 종료
f.close()

#  <div class="card-desc">
#       <h2 class="card-title">아이폰13pro</h2>
#       <div class="card-price ">
#         300,000원
#       </div>
#       <div class="card-region-name">
#         부산 