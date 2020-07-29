#-- 제어문 관련 유용 함수: filter
# - filter(<function>|None, 시퀀스 객체)
# ● 함수의 결과 값이 참인 시퀀스 객체의 이터레이터를 반환
# ● None이 오는 경우 필터링하지 않음
L = [10, 25, 30]
IterL = filter(None, L)
for i in IterL:
  print('Item: {0}'.format(i))

def GetBiggerThan20(i):
  return i > 20
result = list(filter(GetBiggerThan20, L))
print(result)
result = list(filter(lambda i: i > 25, L))
print(result)