#-- for문
# - 시퀀스형 객체를 순차적으로 순회
# ● '시퀀스형 객체 S'의 각 아이템을 '아이템 I'에 할당
# ● 할당된 아이템 I를 가지고 구문을 수행
# ● 모든 아이템을 순회하거나 break를 만나면 for문이 종료
# 예제) for문
l = ['Apple', 100, 15.23]
for i in l:
  print(i, type(i))

d = { 'Apple': 100, 'Orange': 200, 'Banana': 300 }
for k, v in d.items():
  print(k, v)

#-- for문에서 사용할 수 있는 자료
# ● 문자열, 리스트, 튜플, 딕셔너리
# ● 이터레이터, 제너레이터 객체
# 예제)
l = [10, 20, 30]
iterator = iter(l)
for i in iterator:
  print(i)

#-- for문
# ● 반복문은 2개 이상 중첩해서 사용 가능
for n in [1, 2]:
  print('-- {0} 단 --'.format(n))
  for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print('{0} * {1} = {2}'.format(n, i, n * i))