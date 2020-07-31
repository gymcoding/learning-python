#-- 들여쓰기
# ● 들여쓰기(indentation)는 파이썬 문법의 가장 큰 특징
#   (단, 가독성을 높이지만, 오류가 일어나지 않도록 조심해야 함)
#코드블럭1
#[TAB]코드블럭2
#코드블럭3
#[TAB]코드블럭4

# ● 수치
#   1) int
print(10, 0x10, 0o10, 0b10)
#   2) float
print(type(3.14), type(314e-2))
#   3) complex
x = 3-4j
print(type(x), x.imag, x.real, x.conjugate())
#   4) 연산자
#     - +, -, *, /, //, %, **, =

# ● 문자
#   1) 문자 출력
print('string', "string")
print("""
줄바꿈도
그대로 적용됩니다.
""")
#   2) 문자 출력
#     - \n : 개행(줄바꿈)
#     - \t : 탭
#     - \r : 캐리지 리턴
#     - \0 : 널(Null)
#     - \\ : 문자 '\'
#     - \' : 단일 인용부호(')
#     - \" : 이중 인용부호(")

#   3) +, * 연산자
print('py''thon')
print('py' * 3)
#   4) 인덱싱 & 슬라이싱
print('python'[0])
print('python'[5])
print('python'[1:4])
print('python'[-2:])

# ● 유니코드
#   - 모든 문자열(string)이 기본적으로 유니코드
#   - 유니코드 이외의 인코딩이 있는 문자열은 bytes로 표현
print(type('가'))
print('가'.encode('utf-8'))
print(type('가'.encode('utf-8')))

# ● 리스트
#   - 리스트는 쉽게 값들의 나열이라고 생각
#   - 또한, 인덱싱과 슬라이싱도 가능
colors = ['red', 'green', 'gold']
print(colors)

# ● 튜플
#   - 튜플(tuple)은 리스트와 유사하나, 읽기 전용
#   - 읽기 전용인 만큼 제공되는 함수도 리스트에 비해 적지만, 속도는 그만큼 빠름
#   - 튜플에서 제공되는 메소드는 count, index 정도
#     튜플을 이용하면 'C'와 같은 언어에서는 변수가 하나 더 필요한 swap 예제를 다음과 같이 간단하게 해결할 수 있음
a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)

# ● 딕셔너리
#   - 딕셔너리는 키와 값의 쌍으로 이루어져 있으며, 다음과 같이 정의할 수 있음
d = dict(a=1, b=3, c=5)
print(d)
#   - 새로운 값의 추가나 변경은 다음과 같이 간단하게 새로운 키와 값을 할당하면 됨
color = {'apple': 'red', 'banana': 'yellow'}
color['cherry'] = 'red'
print(color)
color['apple'] = 'green'
print(color)