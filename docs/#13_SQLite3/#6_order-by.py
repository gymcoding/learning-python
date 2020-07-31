#-- 레코드 정렬(order by)
# ● ORDER BY 사용 예제
import sqlite3
con = sqlite3.connect('./commit.db')
cur = con.cursor()
cur.execute("SELECT * FROM PhoneBook ORDER BY Name DESC;")
print(cur.fetchall())
