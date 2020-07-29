#-- 연산자 중복
# ● 연산자 중복
#   ○ 사용자 정의 객체에서 필요한 연산자를 내장 타입과 형태와 동작이 유사하도록 재정의
#   ○ 연산자 중복을 위하여 두 개의 밑줄 문자가 앞뒤로 있는 메소드를 미리 정의함

class GString:
  def __init__(self, init = None):
    self.content = init

  def __sub__(self, str):         # '-' 연산자 중복 정의
    for i in str:
      self.content = self.content.replace(i, '')
    return GString(self.content)
  
  def Remove(self, str):
    return self.__sub__(str)


