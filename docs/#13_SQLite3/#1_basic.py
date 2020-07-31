#-- Sqlite3 란?
# ● 디스크 기반의 가벼운 데이터베이스 라이브러리
# ● 서버가 필요치 않음
# ● 모바일 디바이스에 기본적으로 사용되고 있음
# ● 파이썬에도 기본적으로 포함되어 있음

#-- 모듈 함수
# ● sqlite3.connect(database[timeout, isolation_level, detect_types, factory])
#   - SQLite3 DB에 연결
# ● sqlite3.complete_statement(sql)
#   - SQL 문장에 대해서 True를 반환
# ● sqlite3.register_adapter(type, callable)
#   - 사용자 정의 파이썬 자료형을 SQLite3에서 사용하도록 등록
# ● sqlite3.register_converter(typename, callable)
#   - SQLite3에 저장된 자료를 사용자 정의 자료현으로 변환하는 함수를 등록

#-- Connection 클래스
# ● Connection.cursor() 메서드
#   - Cursor 객체 생성
# ● Connection.commit() 메서드
#   - 현재 트랜잭션의 변경내역을 DB에 반영(commit)함
# ● Connection.rollback() 메서드
#   - 가장 최근의 commit() 이수 지금까지 작업한 내용에 대해서 되돌림
# ● Connection.close() 메서드
#   - DB 연결을 종료
# ● Connection.isolation_level() 메서드
#   - 트랜잭션의 격리 수준(isolation level)을 확인/설정
# ● Connection.execute(sql[, parameters]),
#   Connection.executemany(sql[, parameters])
#   Connection.executescript(sql_script)
#   - 임시 Cursor 객체를 생성하여 해당 execute 계열 메서드를 수행
# ● Connection.create_aggregate(name, num_params, aggregate_class)
#   - 사용자 정의 집계(aggregate) 함수를 생성
# ● Connection.create_collation(name, callalble)
#   - 문자열 정렬시 SQL 구문에서 사용될 이름(name)과 정렬 함수를 지정
# ● Connection.iterdump()
#   - 연결된 DB의 내용을 SQL 질의 형태로 출력

#-- Cursor 클래스
# ● Cursor.execute(sql, [, parameters])
#   - SQL 문장을 실행
# ● Cursor.executemany(sql, dseq_of_parameters)
#   - 동일한 SQL 문장을 파라미터만 변경하며 수행
# ● Cursor.executescript(sql_script)
#   - 세미콜론으로 구분된 연속된 SQL 문장을 수행
# ● Cursor.fetchone()
#   - 조회된 결과(Record Set)로 부터 데이터 1개를 반환
# ● Cursor.fetchmany([size=cursor.arraysize])
#   - 조회된 결과로부터 입력받은 size 만큼의 데이터를 리스트 형태로 반환
# ● Cursor.fetchall()
#   - 조회된 결과 모두를 리스트 형태로 반환

#-- 데이터베이스 연결
# ● 실제 파일을 이용한 Connection 객체 생성
import sqlite3
con = sqlite3.connect('test.db')

# ● 메모리를 이용한 Connection 객체 생성
con = sqlite3.connect(':memory:')

# 예제) Cursor.execute 메서드를 이용하여 SQL문을 수행
con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
cur.execute("INSERT INTO PhoneBook VALUES('Someone', '010-1234-5678');")
name = 'Someone'
# 예제) 인자를 전달하여 SQL문을 수행
phone_number = '010-5678-1234'
cur.execute('INSERT INTO PhoneBook VALUES(?, ?);', (name, phone_number))
# 예제) 사전을 이용한 인자 전달
cur.execute("INSERT INTO PhoneBook VALUES(:inputName, :inputNum);", {"inputNum": phone_number, 'inputName': name})
# 예제) 동일한 문장을 매개변수만 바꾸며 연속적으로 수행하는 경우
datalist = (('Tom', '010-543-5432'), ('DSP', '010-123-1234'))
cur.executemany("INSERT INTO PhoneBook VALUES(?, ?);", datalist)

# ● 레코드 조회
# 예제) fetch를 이용한 레코드 조회 방법
cur.execute("SELECT * FROM PhoneBook;")
for row in cur:
  print(row)
# 예제) fetchall의 사용법
cur.execute("SELECT * FROM PhoneBook;")
print(cur.fetchone())
print(cur.fetchall())


