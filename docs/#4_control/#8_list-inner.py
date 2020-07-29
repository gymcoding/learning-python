#-- 리스트 내장
# - [<표현식> for <아이템> in <시퀀스 객체>]
# ● 기존 시퀀스 객체를 이용하여 추가적인 연산을 통하여 새로운 리스트 객체를 생성
# 예제)
l = [1, 2, 3, 4, 5]
print(type(l))
result = [i ** 2 for i in l]
print(result, type(result))

t = ('orange', 'apple', 'banana')
print(type(t))
result = [len(i) for i in t]
print(result, type(result))

#-- 리스트 내장 조건식
# - [<표현식> for <아이템> in <시퀀스 객체> (if <조건식>)]
# ● 조건식을 이용하여 원본 객체에서 조건을 만족하는 아이템만 선별
t = ('orange', 'apple', 'banana', 'kiwi')
result = [i for i in t if len(i) > 5]
print(result)
L_1 = ['a', 'b', 'c']
L_2 = ['A', 'B', 'C']
result = [x + y for x in L_1 for y in L_2]
print(result)