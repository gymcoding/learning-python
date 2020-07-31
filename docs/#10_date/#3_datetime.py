#-- datetime 모듈이란?
# ● 기념일과 같은 날짜, 시간 연산을 위하여 사용
#   예제) - 애인과 사귀기 시작한 날짜로 부터 100일은 언제일까?
#        - 오늘로부터 1000일 후는 무슨 요일일까?

#-- datetime 주요 클래스
# ● datetime.date       - 일반적으로 사용되는 그레고리안 달력의 년, 월, 일을 표현
# ● datetime.time       - 시간을 시, 분, 초, 마이크로 초, 시간대(Time zone)로 표현
# ● datetime.datetime   - date 클래스와 time 클래스의 조합으로 구성
# ● datetime.timedelta  - 두 날짜 혹은 시간 사이의 기간을 표현

#-- date 클래스
# ● 생성자
#   - datetime.date(year, month, day)
# ● 입력인자의 조건
#   - datetime.MINYEAR(1) <= year <= datetime.MAXYEAR(9999)
#   - 1 <= month <= 12
#   - 1 <= day <= 해당 월의 날짜

#-- time 클래스
# ● 시, 분, 초와 같은 시간을 표시
# ● 생성자
#   - datetime.time(hour[, minute[, second[, microsecond[, tzinfo]]]])
# ● 시, 분, 초, 마이크로초, 시간대 정보를 입력 받아서 time 객체를 생성

#-- timedelta 클래스
# ● 두 날짜 혹은 시간 사이의 기간을 표현함
# ● 생성자
#   - timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])

#-- datetime 클래
#   [date클래스 + time클래스]
#-- 시간 연산 예제(1)
from datetime import timedelta
import datetime
td_1 = timedelta(hours = 7)
td_2 = timedelta(hours = -3)
print(td_1 + td_2)
print(datetime.timedelta(-3, 25200))
print(datetime.timedelta(3, 25200))
print(datetime.timedelta(1, 14400))
print(datetime.timedelta(0, 8400))
print(datetime.timedelta(3))

#-- 시간 연산 예제(2)
td_1 = timedelta(hours = 7)
td_2 = timedelta(hours = -3)
print(td_1 > td_2)
print(td_1 < td_2)
td_1 = timedelta(hours = 24)
td_2 = timedelta(hours = 86400)
print(td_1 == td_2)

#-- 시간 연산 예제(3)
dt = datetime.datetime.today()
print(dt)
datetime.datetime(2016, 3, 28, 17, 34, 15, 698707)
td = timedelta(days=2, hours=2)
print(dt + td)
datetime.datetime(2016, 3, 26, 15, 34, 15, 698707)
dt2 = dt.replace(month=1, day=4, hour=7)
print(dt2)
datetime.datetime(2016, 1, 4, 7, 34, 15, 698707)
print(dt - dt2)
datetime.timedelta(83, 36000)
print(dt > dt2)
