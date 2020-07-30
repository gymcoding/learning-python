#-- 파일 입출력 - open
# ● 파일 입출력 제어를 보다 세밀하게 하기 위해서는 open() 함수를 통해서 파일을 연 후, 파일 전용 함수들을 이용해서 작업하는 것이 일반적
#   [기본형: 파일객체 = open(file, mode)]
# ● open 함수의 마지막 인자인 mode는 파일을 열 때의 속성을 의미하며, 다음 속성들의 조합으로 사용이 가능함
#   ○ r: 읽기 모드 (디폴트)
#   ○ w: 쓰기 모드
#   ○ a: 쓰기 + 이어쓰기 모드
#   ○ +: 읽기 + 쓰기 모드
#   ○ b: 바이너리 모드
#   ○ t: 텍스트 모드 (디폴트)

#-- 파일 입출력 - write, close
# ● 파일로부터 읽고 쓰기 위해서 파일로부터 모든 데이터를 읽는 read() 함수와 문자열을 쓰는 write() 함수가 제공됨
# ● 또한 파일을 열고 할 일을 모두 완료했을 경우 파일객체를 닫아주는 close() 함수가 있음
f = open('test.txt', 'w')
f.write('plow deep\nwhile sluggards sleep')
f.close()

#-- 파일 입출력 - read
# ● 텍스트 모드에서는 일반 문자열과 같이 encoding이 적용되기 때문에, 바이너리 데이터(binary data)를 다룰 때에는 오류가 발생함
# ● 바이너리 데이터를 다룰 떼에는 반드시 바이너리 모드를 사용함
f = open('test.txt')
print(f.read())
f.close()
print(f.closed)

#-- 파일 입출력 - readline, readlines, tell, seek
# ● 파일 입출력 관련 함수들
#   ○ readline() 함수 - 호출할 때 마다 한 줄씩 읽은 문자열을 반환함
#   ○ readlines() 함수 - 파일의 모든 내용을 줄 단위로 잘라서 리스트를 반환함
#   ○ tell() 함수 - 현재 파일에서 어디까지 읽고 썼는지 위치를 반환함
#   ○ seek() 함수 - 사용자가 원하는 위치로 포인터를 이동함

# ● with ~ as 구문
with open('test.txt') as f:
  print(f.readlines())
  print(f.closed)
print(f.closed)
