#-- time 모듈
# ● 시간을 표현하는데 사용
# 1) time.time()            - 1970년 1월 1일 자정 이후로 누적된 초를 float 단위로 반환
# 2) time.sleep(secs)       - 현재 동작 중인 프로세스를 주어진 초만큼 정지
# 3) time.gmtime([secs])    - 입력된 초를 변환하여, UTC 기준의 struct_time 시퀀스 객체로 반환
# 4) time.localtime([secs]) - 입력된 초를 변환하여, 지방표준시 기준의 struct_time 시퀀스 객체를 반환
# 5) time.asctime([t])      - struct_time 시퀀스 객체를 인자로 받아서 'Sun Mar 15 18:49:28 2009'와 같은 형태로 반환
# 6) time.mktime(t)         - 지방표준시인 struct_time 시퀀스 객체를 인자로 받아서 time()과 같은 누적된 초를 반환
import time
print(time.time())
print(time.gmtime())
print(time.localtime())

t = time.gmtime(1234567890)
print(t)
print(t.tm_mon)
print(t.tm_hour)
print(time.asctime(t))
print(time.mktime(t))

#-- strptime, strftime
# ● 사용자가 직접 포맷을 지정하여 출력
# ● 함수 원형
#   time.strftime(format[, t])
#   time.strftime(string[, format])
# ● 형식 지시자
# 1) %y - 연도를 축약하여 표시
# 2) %Y - 연도를 축약하지 않고 표시
# 3) %b - 축약된 월 이름
# 4) %B - 축약되지 않은 월 이름
# 5) %m - 숫자로 표현한 월(01~12)
# 6) %d - 일(01~31)
# 7) %H - 24시를 기준으로 한 시(00~23)
# 8) %I - 12시를 기준으로 한 시(01~12)
# 9) %M - 분(00~59)
# 10) %S - 초(00~61)
# 11) %p - AM/PM
# 12) %a - 축약된 요일 이름
# 13) %A - 축약되지 않은 요일 이름
# 14) %w - 요일을 숫자로 표시
# 15) %j - 1월 1일 부터 누적된 날짜(001~366)

#-- strftime 예제 코드
from time import localtime, strftime
result = strftime('%B %dth %A %I:%M', localtime())
print(result)
result = strftime('%Y-%m-%d %I:%M', localtime())
print(result)
result = strftime('%y/%m/%d %H:%M:%S', localtime())
print(result)
result = strftime('%y/%m/%d %H:%M:%S')
print(result)

#-- strptime 예제 코드
from time import strptime
timestring = time.ctime(1234567890)
print(timestring)
result = strptime(timestring)
print(result)
result = strptime(timestring, '%a %b %d %H:%M:%S %Y')
print(result)
# result = strptime(timestring, '%a %b %d %H:%M:%S %y') # ValueError: unconverted data remains: 09
# print(result)