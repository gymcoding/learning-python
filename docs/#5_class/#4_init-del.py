#-- 생성자와 소멸자
# ● 생성자
# - 생성시 초기화 작업을 수행
# - 인스턴스 객체가 생성될 때 자동으로 호출
# - __init__()
# ● 소멸자
# - 소멸시 종료 작업을 수행
# - 인스턴스 객체의 참조 카운터가 '0'이 될 때 호출
# - __del__()

class MyClass:
  def __init__(self, value):      # 생성자 메소드
    self.Value = value
    print('Class is created! Value = ', value)
  def __del__(self):              # 소멸자 메소드
    print('Class is deleted!')

def foo():
  d = MyClass(10)                 # 함수 foo 블록안에서만 인스턴스 객체 d가 존재
  print(d)

foo()



