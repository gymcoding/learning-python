#-- 데이터베이스 덤프 만들기
# 예제) 데이터베이스 덤프 예제 코드
import sqlite3
con = sqlite3.connect(':memory:')
cur = con.cursor()

cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
cur.execute("INSERT INTO PhoneBook VALUES('Derick', '010-1234-5678');")
list = (('Tom', '010-543-5432'), ('DSP', '010-123-1234'))
cur.executemany("INSERT INTO PhoneBook VALUES(?, ?);", list)

for l in con.iterdump():
  print(l)