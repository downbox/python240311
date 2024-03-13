# web1.py
# 웹크롤링을 위한 선언
from bs4 import Beautifulsoup

# 페이지를 로딩
page = open("test01.html", "rt", encoding="utf-8").read()

# 검색이 용이한 객체 생성
soup = Beautifulsoup(page, "html.parser")
print(soup.prettify())