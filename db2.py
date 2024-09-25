#db2.py

import sqlite3

#영구적으로 파일에 저장(커밋 저장)
con = sqlite3.connect("c:\\수업자료\\work\\sample.db")
#sql구분은 커서객체 실행
cur = con.cursor()
#테이블 구조를 생성(테이블 스키마)
cur.execute("create table  if not exists PhoneBook (Name text, PhoneNum text);")

cur.execute("insert into PhoneBook values ('김길동','010-1212-3333');")
#입력파라메터 처리
name = '전우치'
phoneNumber = '010-1233-9999'
cur.execute("insert into PhoneBook values (?,?);",(name,phoneNumber))

datalist = (("박문수",'010-312-3333'),("홍길동",'010-312-9999'))
cur.executemany("insert into PhoneBook values (?,?);", datalist)

#검색
cur.execute("select * from PhoneBook where Name like '%';")

for row in cur:
    print(row[0],row[1])

#완료
con.commit()
