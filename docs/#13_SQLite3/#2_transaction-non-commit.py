#-- 트랜잭션 처리
# 예제) 작업한 내용이 커밋되지 않는 예제
import sqlite3
con = sqlite3.connect('./test.db')
cur = con.cursor()
cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
cur.execute("INSERT INTO PhoneBook VALUES('Derick', '010-1234-5678');")
cur.execute("SELECT * FROM PhoneBook;")
print(cur.fetchall())