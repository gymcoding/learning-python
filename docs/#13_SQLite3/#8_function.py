#-- 내장/집계 함수
# 1) abs(x)     - 절대값을 반환
# 2) length(x)  - 문자열의 길이를 반환
# 3) lower(x)   - 소문자로 변환해서 반환
# 4) upper(x)   - 대문자로 변환해서 반환
# 5) min(...)   - 최소값을 반환
# 6) max(...)   - 최대값을 반환
# 7) random(*)  - 임의의 정수를 반환
# 8) count(x)   - NULL이 아닌 튜플의 개수를 반환
# 9) count(*)   - 튜플의 개수를 반환
# 10) sum(x)    - 합을 반환

#-- 자료형
# ● SQLite3 자료형과 그에 대응되는 파이썬의 자료형
#   [SQLite3]     [파이썬]
#   ○ NULL        ○ None
#   ○ INTEGER     ○ int
#   ○ REAL        ○ float
#   ○ TEXT        ○ str, float
#   ○ BLOB        ○ buffer
import sqlite3
con = sqlite3.connect('./commit.db')
cur = con.cursor()
cur.execute("CREATE TABLE tbl_1(Name TEXT, Age INTEGER, Money REAL);")
cur.execute("CREATE TABLE tbl_2(Name str, Age int, Money flat);")