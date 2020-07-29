#-- 클래스와 인스턴스 관계
# - isinstance(인스턴스 객체, 클래스 객체)
# ● 인스턴스 객체가 어떤 클래스로부터 생성되었는지 확인
# ● bool 형태로 결과 반환
class Person:
  pass

class Bird:
  pass

class Student(Person):
  pass

p, s = Person(), Student()
print('p is instance of Person: ', isinstance(p, Person))
print('s is instance of Person: ', isinstance(s, Person))
print('p is instance of object: ', isinstance(p, object))
print('p is instance of Bird: ', isinstance(p, Bird))
