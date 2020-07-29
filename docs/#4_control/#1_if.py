#-- if
#   ● 조건식을 평가하고 참인 경우만 구문이 수행
#   ● 2개 이상의 구문은 들여쓰기로 블록을 지정
#     ○ 함수와 동일
#     ○ 들여쓰기의 정도는 파일 전체를 통틀어 일치해야 함

# 예제
value = 10
if value > 5:
  print('value is bigger than 5')

#-- elif, else
#   1. elif
#     ● 2개 이상의 조건을 처리하는 경우
#     ● if는 가장 처음에만 사용할 수 있는 반면에, elif는 필요한 만큼 사용 가능

#   2. else
#     ● 어떠한 조건에도 해당하지 않는 경우
#     ● 가장 마지막에만 사용 가능

# 예제
score = int(input('Input Score: '))
if 90 <= score <= 100:
  grade = 'A'
elif 80 <= score < 90:
  grade = 'B'
elif 70 <= score < 80:
  grade = 'C'
elif 60 <= score < 70:
  grade = 'D'
else:
  grade = 'F'
print('Grade is ', grade)

"""
3. 파이썬의 조건식 표현방법
● 70 <= score < 80
● grade >= 70 and grade < 80
"""