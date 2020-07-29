#-- 제어문 관련 유용 함수: map
# - map(<function>, 시퀀스 객체, ...)
# ● 시퀀스 객체를 순회하며 function의 연산을 수행
# ● 함수의 인자 수만큼 시퀀스 객체를 전달
L = [1, 2, 3]
def Add10(i):
  return i + 10

result = map(Add10, L)
for i in result:
  print('Item: {0}'.format(i))


X = [1, 2, 3]
Y = [2, 3, 4]
result = list(map(pow, X, Y))
print(result)
