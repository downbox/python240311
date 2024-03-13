# web1.py
# 웹크롤링을 위한 선언
from bs4 import BeautifulSoup

# 페이지를 로딩
page = open("test01.html", "rt", encoding="utf-8").read()

# 검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())

# 문서의 <p>전체 검색
# print(soup.find("p"))
# print(soup.find_all("p"))

# 조건이 있는 경우 : <p class='outer-text'> 컨텐트</p>
# class 키워드와 충돌이 발생하므로 class_ 를 사용
# print(soup.find_all("p", class_="outer-text"))
# print(soup.find_all("p", attrs={"class":"outer-text"}))

# 태그의 내부 문자열만 가져오기 : .text 속성
# for tag in soup.find_all("p"):
#     title = tag.text.strip()
#     title = title.replace("\n","")
#     print(title)

print(soup.find(id=="first"))
