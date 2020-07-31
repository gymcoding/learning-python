#-- 레코드 정렬(order by)
# ● ORDER BY 사용 예제
import sqlite3
con = sqlite3.connect('./commit.db')
cur = con.cursor()

# ● 사용자 임의로 정렬 방식을 변경하는 경우
def OrderFunc(str1, str2):  # 대소문자 구별 없이 정렬하는 함수
  s1 = str1.upper()
  s2 = str2.upper()
  return (s1 > s2) - (s1 < s2)
con.create_collation('myordering', OrderFunc) # SQL 구문에서 호출할 이름과 함수를 등록
cur.execute('SELECT Name FROM PhoneBook ORDER BY Name COLLATE myordering')
print([r[0] for r in cur])


