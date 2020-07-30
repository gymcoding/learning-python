#-- 포매팅(formatting)
# ● print만으로는 출력이 좀 불편하다고 느낄 수 있으나 format() 메소드를 사용하면 문자열을 그 이상으로 자유롭게 다루 수 있음
# ● 문자열 내에서 어떤 값이 들어가길 원하는 곳은 {}로 표시함
# ● {} 안의 값들은 숫자로 표한할 수 있으며, format 인자들의 인덱스를 사용함
# ● {0}는 첫 번째 인자인 'apple'을 나타내고
# ● {1}는 첫 번째 인자인 'red'을 나타내고
print('{0} is {1}'.format('apple', 'red'))

#-- 포매팅(formatting) - 키, 사전 이용
# ● {} 안의 값을 지정할 때는 다음과 같이 format의 인자로 키(key)와 값(value)을 주어 위와 동일한 결과를 얻을 수 있음
print('{item} is {color}'.format(item = 'apple', color = 'red'))
# ● dictionary를 입력으로 받는 경우
dic = {'item': 'apple', 'color': 'red'}
print('{0[item]} is {0[color]}'.format(dic))

#-- 포매팅(formatting) - **사용
# ● **기호를 사용하면 dictionary를 입력으로 받은 것으로 판단하고 인자를 하나만 받게 됨
# ● 불필요한 index를 생략 가능
print('{item} is {color}'.format(**dic))

#-- 포매팅(formatting) - 문자열 변환
# ● ! 기호를 사용해서 문자열 변환을 사용할 수 있음
print('{item!s} is {color!s}'.format(**dic))
print('{item!r} is {color!r}'.format(**dic))
print('{item!a} is {color!a}'.format(**dic))
# !s, !r, !a는 각각 str(), repr(), ascii()를 실행한 결과와 동일

#-- 포매팅(formatting) - 사용법
# ● ":" 기호를 이용하여 보다 정교하게 정렬, 폭, 부호, 공백처리, 소수점, 타입 등을 지정하는 방법
print('{0:$>5}'.format(10))

#-- 포매팅(formatting) - 정렬과 부호 표현법
# ● 정렬에 사용되는 기호
#   ○ ">" 오른쪽 기준
#   ○ "<" 왼쪽 기준
#   ○ "^" 가운데 기준
# "="가 사용되면 공백문자들 앞에 부호가 표시됨. 사용되지 않으면 공백문자들 뒤, 즉, 숫자 바로 앞에 부호가 표시됨

#-- 포매팅(formatting) - 정렬과 부호 표현법
# ● 부호를 나타내는 기호
#   ○ "+" 플러스 부호를 나타내라는 뜻
#   ○ "-" 마이너스 값만 마이너스 부호를 나타내라는 뜻
#   ○ " " 마이너스 값에는 마이너스 부호를 나타내고 플러스일 때는 공백을 표시하라는 뜻
print('{0:$>-5}'.format(-10))

#-- 포매팅(formatting) - 진수 표현법
# ● 진수를 바꿔서 출력
#   ○ 'b'는 이진수를, 'd'는 십진수를, 'x'는 16진수를, 'o'는 8진수를 나타내며 'c'는 문자열을 출력
print('{0:b}'.format(10))
print('{0:o}'.format(10))
print('{0:c}'.format(65))
#   ○ '#'을 사용하면 #x는 16진수 #o는 8진수, #b는 2진수로 표시됨
print('{0:#x}, {0:#o}, {0:#b}'.format(10))

#-- 포매팅(formatting) - 실수 표현법
# ● 정수 이외에 실수에 대한 변환도 제공되며, 'e'는 지수표현은 'f'는 일반적인 실수 표현을, '%'는 퍼센트 표현을 의미
print('{0:e}'.format(4 / 3))
print('{0:f}'.format(4 / 3))
print('{0:%}'.format(4 / 3))

#-- 포매팅(formatting) - 실수 표현법
# ● 실수에서는 소수점 몇 번째 자리까지 표현할 것인지를 지정가능
print('{0:.3f}'.format(4 / 3))
