#-- sys 모듈

# ● sys.argv
#   - 파이썬 스크립트로 넘어온 입력 인자(argument)들의 리스트
import sys
print('argv size: ', len(sys.argv))
for i, arg in enumerate(sys.argv):
  print(i, arg)

# ● sys.exc_info
#   - 현재 발생한 예외 정보를 튜플로 반환
import sys
print(sys.exc_info())
try:
  1/0
except:
  exc_class, val, tb_ob = sys.exc_info()
  print(exc_class)
  print(val)
  print(tb_ob)

# ● sys.exit
#   - 프로세스를 종료

# ● sys.path
#   - 모듈을 찾을 때 참조하는 경로를 나타냄
print(sys.path)
