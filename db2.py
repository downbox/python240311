# db1.py
import sqlite3

# 연결 인스턴스
# con = sqlite3.connect(":memory:")
con = sqlite3.connect("c:\\work\\sample.db")

# 커서 인스턴스 (실제 구문 실행)
cur = con.cursor()

# 테이블 구조 생성
cur.execute("create table if not exists PhoneBook (name text, phoneNum text);")

# 입력 파라메터 처리
name = "박문수"
phoneNum = "010-123"
cur.execute("insert into PhoneBook values (?,?);", (name, phoneNum))

# 1건 데이터 입력
# cur.execute("insert into PhoneBook value ('홍길동','010-222');")
cur.execute("INSERT INTO PhoneBook VALUES ('홍길동', '010-222');")

# 여러건 입력
dataList = (("tom", "020-222"),("eir","222-111"))
cur.executemany("insert into PhoneBook values (?,?);", dataList)

# 검색
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)

print(cur.fetchone())
print(cur.fetchmany(2))

# 작업완료(쓰기)
con.commit()