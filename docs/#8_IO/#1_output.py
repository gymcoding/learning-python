#-- 출력
# ● 화면으로 출력할 때는 print() 함수 사용
#   - 파이썬 버전 2.x 때는 print가 함수가 아니었지만, 3.0에서는 함수로 바뀜
# ● 즉, 다음과 가이 함수처럼 괄호 안에 출력할 인자를 적음
print(1)
print('hi, guyz')

# ● print 함수의 입력인자로 다음과 같이 구분자(sep), 끝라인(end), 출력(file)을 지정해 줄 수 있음
# ● 아래 예제와 같이 file을 이용해서 출력을 표준오류(StandardError)로 변경하거나 파일로 바꿀 수도 있음
import sys
print('welcome to', 'python', sep = '~', end = '!', file = sys.stderr)