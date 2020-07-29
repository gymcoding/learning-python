#-- 상속
# ● 부모 클래스의 모든 속성(데이터, 메소드)를 자식 클래스로 물려줌
# ● 클래스의 공통된 속송을 부모 클래스에 정의
# ● 하위 클래스에서는 특화된 메소드와 데이터를 정의

# ● 장점
#   ○ 각 클래스마다 동일한 코드가 작성되는 것을 방지
#   ○ 부모 클래스에 공통된 속성을 두어 코드의 유지 보수가 용이
#   ○ 각 개별 클래스에 특화된 기능을 공통된 인터페이스로 접근 가능

# 예제)
class Person:
  def __init__(self, name, phoneNumber):
    self.Name = name
    self.PhoneNumber = phoneNumber

class Student(Person):
  def __init__(self, name, phoneNumber, subject, studentID):
    self.Name = name
    self.PhoneNumber = phoneNumber
    self.Subject = subject
    self.StudentID = studentID

# ● 클래스 간의 관계 확인
#   - issubclass(자식 클래스, 부모 클래스)
print(issubclass(Student, Person))

#-- 다중상속
# ● 2개 이상의 클래스를 상속받는 경우
# ● 두 클래스의 모든 속성(변수와 메소드)을 전달받음
class Tiger:
  def Jump(self):
    print('호랑이처럼 멀리 점프하기')

class Lion:
  def Bite(self):
    print('사자처럼 한입에 꿀꺽하기')

class Liger(Tiger, Lion):   # 다중 상속
  def Play(self):
    print('라이거만의 사육사와 재미있게 놀기')

liger = Liger()
liger.Play()
liger.Jump()
liger.Bite()

#-- 클래스 상속과 이름 공간(namespace)
# ● 인스턴스 객체 영역
#   ○ 클래스 객체 간 상속을 통한 영역(자식 클래스 영역, 부모 클래스 영역)
# ● 전역 영역
class SuperClass:             # 부모 클래스
  x = 10
  def printX(self):
    print(self.x)

class SubClass(SuperClass):   # 자식 클래스
  y = 20
  def printY(self):
    print(self.y)

s = SubClass()
s.a = 30

# [메모리]
# SuperClass(클래그 객체)
# - x
# - printX

# [메모리]
# SubClass(클래그 객체)
# - y
# - printY

# [메모리]
# s(인스턴스 객체)
# - a
