#-- 클래스와 인스턴스 이름 공간
# ● 검색순서
#   [인스턴스 객체 영역] -> [클래스 객체 영역] -> [전역 영역]

class Person:                 # 클래스 정의
  name = 'Default Name'

p1 = Person()
p2 = Person()
print('p1 is name: {0}'.format(p1.name))
print('p2 is name: {0}'.format(p2.name))
p1.name = '김연아'              # p1 인스턴스의 'name' 속성을 변경
print('p1 is name: {0}'.format(p1.name))
print('p2 is name: {0}'.format(p2.name))

#-- 클래스와 인스턴스에 멤버 데이터 추가
Person.title = 'New title'    # 클래스 객체에 새로운 멤버 변수 title 추가
p1.age = 20                   # p1 객체에만 age 멤버 변수를 추가
print('p1\'s title: ', p1.title)
print('p1\'s age: ', p1.age)
print('p2\'s title: ', p2.title)
print('p2\'s age: ', p2.age)