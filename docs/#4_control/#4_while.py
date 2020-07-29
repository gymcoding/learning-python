#-- while문
# - 조건식이 참(True)인 동안 내부 구문을 반복 수행
# ● 조건식은 구문이 수행되기 이전에 우선 평가
# ● 구문을 모두 수행 이후 다시 조건식을 재평가
# ● 조건식이 거짓(False)이면 while문 구조를 벗어남

# 예제) while문
value = 5
while value > 0:
  print(value)
  value -= 1