#-- 제어문 관련 유용 함수: range
# - range(['시작값'], '종료값'[, '증가값'])
# ● 수열을 순회하는 이터레이터 객체를 반환
# ● 시작 값과 증가 값은 생략 가능하며, 이때는 각 0, 1이 할당
result = list(range(10))
print(result)
result = list(range(5, 10))
print(result)
result = list(range(10, 0, -1))
print(result)
result = list(range(10, 20, 2))
print(result)