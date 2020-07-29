#-- class란?
# ● 데이터와 데이터를 변형하는 함수를 같은 공간으로 작성
# - 메서드(Method)
# - 인스턴스(Instance)
# - 정보 은닉(Information Hiding)
# - 추상화(Abstraction)

#-- 클래스와 인스턴스
class Person:             # 클래스 정의
  Name = 'Default Name'   # 멤버 변수

  def Print(self):        # 멤버 메소드
    print('My Name is {0}'.format(self.Name))

p1 = Person()             # 인스턴스 객체 생성
p1.Print()                # 멤버 변수값을 출력
