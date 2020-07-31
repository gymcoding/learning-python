#-- 클래스
# ● # 클래스와 인스턴스
class Person:           # 클래스 정의
  Name = 'Default Name' # 멤버 변수

  def print(self):      # 멤버 메소드
    print('My Name is {0}'.format(self.Name))

p1 = Person()           # 인스턴스 객체 생성
p1.print()              # 멤버 변수값을 출력

# ● 생성자와 소멸자
#   ○ 생성자
#     - 생성 시 초기화 작업을 수행
#     - 인스턴스 객체가 생성될 때 자동으로 호출
#     - __init__()
#   ○ 소멸자
#     - 소멸 시 종료 작업을 수행
#     - 인스턴스 객체의 참조 카운터가 '0'이 될 때 호출
#     - __del__()

# ● 모듈 임포트 방법
#   ○ from <모듈> import <어트리뷰트>
#   ○ from <모듈> import *
#   ○ import <모듈> as <별칭>
#     - <모듈> 이름을 <별칭>으로 변경하여 임포트

# ● 예외 처리
#   ○ try 구문
#     try:
#     except <예외 종류>:
#       <예외 처리 문장>
#     except (예외1, 예외2):
#       <예외 처리 문장>
#     except 예외 as 인자:
#       <예외 처리 문장>
#     else:
#       <예외가 발생하지 않은 경우, 수행할 문장>
#     finally:
#       <예외 발생 유무에 상관없이 try 블록 이후 수행할 문장>

# ● 출력
#   ○ print 함수의 입력인자로 다음과 같이 구분자(sep), 끝라인(end), 출력(file)을 지정해 줄 수 있음
#   ○ 아래 예제와 같이 file을 이용해서 출력을 표준요류(Standard Error)로 변경하거나 파일로 바꿀 수 있음
import sys
print('welcome to', 'python', sep='~', end='!', file=sys.stderr)

# ● 입력
#   ○ 사용자로부터 입력은 다음과 같이 input() 함수를 이용해서 받을 수 있음
#   ○ input의 입력 인자로는 화면에 출력할 프롬프트(prompt)를 줄 수 있으며, 생략 가능
#   ○ 결과값으로는 문자열 객체를 반환
# a = input('insert any keys : ')
# print(a)

# ● 파일 입출력 - open
#   - open 함수의 마지막 인자인 mode는 파일을 열 때의 속성을 의미하며, 다음 속성들의 조합으로 사용이 가능함
#     1) r: 읽기모드
#     2) w: 쓰기모드
#     3) a: 쓰기 + 이어쓰기 모드
#     4) +: 읽기 + 쓰기 모드
#     5) b: 바이너리 모드
#     6) t: 텍스트 모드 (디폴트)

# ● 파일 입출력 - write, close
#   - 파일로부터 읽고 쓰기 위해서 파일로부터 모든 데이터를 읽는 read() 함수와 문자열을 쓰는 write() 함수가 제공됨
#   - 파일을 열고 할 일을 모두 완료했을 경우 파일 객체를 닫아주는 close() 함수가 있음
f = open('test.txt', 'w')
f.write('plow deep\nwhile sluggards sleep')
f.close()

# ● 파일 입출력 - read
f = open('test.txt')
print('### start test.txt ###')
print(f.read())