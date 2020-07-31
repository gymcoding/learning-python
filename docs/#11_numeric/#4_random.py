#-- 여러가지 random 메서드
# 1) random.seed([x]) - 임의 숫자 생성기의 초기화 작업을 함
# 2) random.random() - '0.0 <= F < 1.0' 사이의 임의의 float 숫자를 반환
# 3) random.uniform(a, b) - 인자로 받은 두 값 사이의 임의의 float 숫자를 반환
# 4) random.gauss(m, sb) - 가우스 분포의 난수를 반환
# 5) random.randrange([start], stop[, step]) - 내장 함수인 range()의 아이템 중에서 임의로 선택하여 반환
# 6) random.randint(a, b) - 'a <= N <= b'인 임의의 정수 N을 반환
# 7) random.choice(seq) - 입력받은 시퀀스 객체의 임의의 아이템을 반환
# 8) random.shufle(x[, random]) - 입력받은 시퀀스 객체를 섞음
# 예제1)
import random
print(random.random())
print(random.random())
print(random.uniform(3, 4))
for i in range(3):
  print('for i={0}'.format(i))
  print(random.gauss(1, 1.0))
# 예제2)
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20), 10))
# 예제3)
l = list(range(10))
print(l)
print([random.choice(l) for i in range(3)])
print(random.sample(l, 3))
l2 = list(range(10))
print(l2)
random.shuffle(l2)
print(l2)