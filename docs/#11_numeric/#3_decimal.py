#-- 부동 소수점 표현 방식
#   [정수] - 고정 소수점 방식
#   [실수] - 부동 소수점 방식
# ● 소수점의 위치를 고정하지 않고, 그 위치를 나타내는 수를 따로 적는 방식
# ● 유효숫자를 나타내는 가수와 소수점의 위치를 풀이하는 지수로 나누어서 표현
# ● '[가수] * [밑수]^[지수]와 같은 형태
# ● 컴퓨터 시스템은 밑수를 2로 하고, 부호를 나타내는 하나의 비트를 추가하여 그림과 같이 세 부분으로 나누어서 실수를 표현

#-- 부동 소수점의 문제
# ● 실수 표현의 문제
print(0.1)  # 0.10000000001 로 나와야 하지만 0.1로 정상 출력
print(1/3)  # 0.33333333331 로 나와야 하지만 0.333333333333로 정상 출력
# ● 결합법칙 예제
print((1234.567 + 45.67844) + 0.0004)
print(1234.567 + (45.67844 + 0.0004))
# ● Decimal 객체 생성
#   ○ 생성자
#     decimal.Decimal([value[, context]])
# 예제)
import decimal
print(decimal.Decimal(3))                   # 정수
print(decimal.Decimal('1.1'))               # 문자열
print(decimal.Decimal((0, (3, 1, 4), -2)))  # 튜플
print(decimal.Decimal('-Infinity'))         # 음의 무한대
print(decimal.Decimal('NaN'))               # NaN(Not a Number)
# ● 모든 수치 연산과 내장 함수의 인자로 전달 가능
import decimal
a, b = decimal.Decimal('3.14'), decimal.Decimal('.04')
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)

# ● max, min, sum과 같은 내장 함수의 인자로도 전달 가능
raw_data = '3.45|5.3|1.65|9|-1.28'
l = [decimal.Decimal(x) for x in raw_data.split('|')]
print(l)
print(max(l))
print(min(l))
print(sum(l))
print(sorted(l))

