#db1.py

import sqlite3

#메모리에 임시로 저장
con = sqlite3.connect(":memory:")
#sql구분은 커서객체 실행
cur = con.cursor()
#테이블 구조를 생성(테이블 스키마)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")

cur.execute("insert into PhoneBook values ('김길동','010-1212-3333');")
#입력파라메터 처리
name = '전우치'
phoneNumber = '010-1233-9999'
cur.execute("insert into PhoneBook values (?,?);",(name,phoneNumber))

datalist = (("박문수",'010-312-3333'),("홍길동",'010-312-9999'))
cur.executemany("insert into PhoneBook values (?,?);", datalist)

#검색
cur.execute("select * from PhoneBook where Name like '%';")

# for row in cur:
#     print(row[0],row[1])
print("--fatchone()----")
print(cur.fetchone())
print("--fatchmany()----")
print(cur.fetchmany())
print("--fatchall()----")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())