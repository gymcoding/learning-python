#-- Fraction 클래스
# ● 유리수와 관련된 연산을 효율적으로 처리할 수 있는 분수(fractions)모듈
# ● Fraction 클래스의 생성자
#   ○ fraction Fraction(분자=0, 분모=1)
#   ○ fraction Fraction(Fraction 객체)
#   ○ fraction Fraction(문자열)
import fractions
fraction_obj1 = fractions.Fraction(4, 16)
print(fraction_obj1)
fraction_obj2 = fractions.Fraction(3)
print(fraction_obj2)
fraction_obj3 = fractions.Fraction('3.14')
print(fraction_obj3)

#-- 지원 메서드
# ● 기본적인 연산 및 floor, ceil, round도 사용 가능하며, 최대공약수를 반환하는 클래스 메서드도 존재
f = fractions.Fraction.from_float(3.14)
print(f.__floor__())
import math
print(math.floor(f))
print(math.ceil(f))
print(round(f))