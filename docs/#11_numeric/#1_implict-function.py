#-- 내장함수
# 1) sum(iterable[, start]) - 순회 가능한(iterable) 객체의 총 합계를 반환
# 2) max(iterable) - 순회 가능한 객체의 최댓값을 반환
# 3) min(iterable) - 순회 가능한 객체의 최솟값을 반환
# 4) abs(x) - x의 절대값을 반환
# 5) pow(x, y, [, z]) - x의 y 제곱 값을 반환
# 5) round(x, [, n]) - x의 반올림 결과를 반환
# 5) divmod(a, b) - 'a/b'의 몫과 나머지를 튜플 형태로 반환'
# 예제)
l = list(range(0, 10))
print(l)
print(sum(l))
print(max(l))
print(min(l))
print(abs(-11))
print(pow(2, 10))

#-- math 모듈의 수치 연산 함수들
# 1) math.ceil(x) - 'N >= x'를 만족하는 가장 작은 정수 N을 반환
# 2) math.floor(x) - 'N >= x'를 만족하는 가장 큰 정수 N을 반환
# 3) math.trunc(x) - x의 정수 부분만을 반환
# 4) math.copysign(x, y) - y의 부호만 x에 복사하여 반환
# 5) math.fabs(x) - x의 절대값을 반환
# 6) math.factorial(x) - x의 계승(factorial, x!) 값을 반환
# 7) math.fmod(x, y) - 나머지 연산을 수행
# 8) math.fsum(iterable) - 입력받은 값의 합계를 반환
# 9) math.modf(x) - 입력받은 x의 순수 소수부분과 정수 부분으로 분리하여 튜플로 반환
# 예제)
import math
print(math.ceil(3.14))
print(math.floor(3.14))
print(math.trunc(3.14))
print(math.fmod(5.5, 3))
print(math.fmod(-5.5, 3))

#-- math 지수, 로그 연산
# 1) math.pow(x, y) - x의 y제곱한 결과를 반환
# 2) math.sqrt(x) - x의 제곱근(square root)한 결과를 반환
# 3) math.exp(x) - 'e^x'의 결과를 반환
# 4) math.log(x[] base]) - 밑은 base로 하는 logX의 결과를 반환

#-- 삼각함수 연산
# 1) math.degrees(x) - 라디안으로 표현된 각도를 60분법으로 변환
# 2) math.radians(x) - 60분법으로 표현된 각도를 라디안으로 변환


