#-- str
# ● 문자열을 다루는 기본 클래스
# ● 특별한 모듈을 import할 필요가 없음(내장 클래스)
# print(dir(str))

# ● capitalize()
result = 'PYTHON'.capitalize()
print(result)
result = 'python is powerful'.capitalize()
print(result)

# ● count(keyword, [start, [end]])
result = 'python is powerful'.count('p')
print(result)
result = 'python is powerful'.count('p', 5) # [5:]으로 슬라이싱하고 count한 결과와 동일
print(result)
result = 'python is powerful'.count('p', 0, -1) # [0:-1]으로 슬라이싱하고 count한 결과와 동일
print(result)

# ● encode([encoding, [errors]])
#   ○ 기본적인 사용법
result = '가나다'.encode('cp949')  # 윈도우에서 사용하는 'CP949'로 변환
print(result)
result = '가나다'.encode('utf-8')  # 윈도우에서 사용하는 'UTF-8'로 변환
print(result)
#   ○ Errors 사용법
# result = '가나다'.encode('latin1', 'strict') # 에러 발생
# print(result)
result = '가나다abc'.encode('latin1', 'ignore')
print(result)
result = '가나다abc'.encode('latin1', 'replace')
print(result)
result = '가나다abc'.encode('latin1', 'xmlcharrefreplace')
print(result)
result = '가나다abc'.encode('latin1', 'backslashreplace')
print(result)

# ● endswith(postfix, [start, [end]])
result = 'python is powerful'.endswith('ful')
print(result)
result = 'python is powerful'.endswith('ful', 5)  # [5:]으로 슬라이싱하고 endswith한 결과와 동일
print(result)
result = 'python is powerful'.endswith('ful', 5, -1) # [5:-1]으로 슬라이싱하고 endswith한 결과와 동일
print(result)
result = 'python is powerful'.endswith(('m', 'l'))
print(result)

# ● expandtabs([tabsize])
print('python\tis\tpowerful')
print('python\tis\tpowerful'.expandtabs())
print('python\tis\tpowerful'.expandtabs(1))

# ● find(keyword, [start, [end]])
result = 'python is powerful'.find('p')
print(result)
result = 'python is powerful'.find('p', 5, -1)  # [5:-1]으로 슬라이싱하고 find한 결과와 동일
print(result)
result = 'python is powerful'.find('pa')        # 키워드를 문자열에서 찾지 못하는 경우
print(result)

# ● index(keyword, [start, [end]])
result = 'python is powerful'.index('p')
print(result)
result = 'python is powerful'.index('p', 5, -1) # [5:-1]으로 슬라이싱하고 index한 결과와 동일
print(result)
# result = 'python is powerful'.index('pa') # 키워드를 문자열에서 찾지 못하는 경우
# print(result)

# ● isalnum()
result = 'python'.isalnum()
print(result)
result = 'python3000'.isalnum()
print(result)
result = 'python3.2'.isalnum()
print(result)

# ● isalpha()
result = 'python'.isalpha()
print(result)
result = 'python3000'.isalpha()
print(result)

# ● islower()
result = 'python'.islower()
print(result)
result = 'Python'.islower()
print(result)
result = 'python3.2'.islower()
print(result)

# ● isspace()
result = ' '.isspace()
print(result)
result = '\t\n '.isspace()
print(result)
result = '\thi\n'.isspace()
print(result)

# ● istitle()
result = 'python is powerful'.istitle()
print(result)
result = 'PYTHON IS POWERFUL'.istitle()
print(result)
result = 'Python Is Powerful'.istitle()
print(result)

# ● isupper()
result = 'Python'.istitle()
print(result)
result = 'PYTHON'.istitle()
print(result)
result = 'PYTHON3.2'.istitle()
print(result)

# ● isdecimal(), isdigit()
result = '2580'.isdecimal()
print(result)
result = '\u0669', '\u0669'.isdecimal()
print(result)
result = '\u00bc', '\u00bc'.isdecimal()
print(result)

# ● isnumeric()
result = '\u00bc', '\u00bc'.isdecimal()
print(result)
result = '\u00bc', '\u00bc'.isnumeric()
print(result)

# ● join(sequence)
result = '.'.join('HOT')
print(result)
result = '\t'.join(['python', 'is', 'powerful'])
print(result)

# ● lower()
# - 대문자로된 String을 소문자로 바꾸는 함수
result = 'python \t'.lower()
print(result)
result = 'Python'.lower()
print(result)

# ● strip()
# - 문자열 왼쪽 제거. chars지정이 없으면 공백문자를 제거. 지정되어 있으면 chars의 모든 조합을 제거
result = '\t\n python'.strip()
print(result)
result = '>>> python is good <<<'.strip('<> ')
print(result)

# ● lstrip()
# - 문자열 양끝제거. charset 지정이 없으면 공백문자를 제거. 지정되어 있으면 chars의 모든 조합을 제거
result = '\t\n python'.lstrip()
print(result)
result = '>>> python is good'.lstrip('> ')
print(result)

# ● rstrip()
# - 문자열 오른쪽 제거. chars지정이 없으면 공백문자를 제거. 지정되어 있으면 chars의 모든 조합을 제거
result = '>>> python is good <<<'.rstrip('><')
print(result)

# ● maketrans()
# - 문자열을 치환해 주는 함수. 숫자가능. 단, 바꾸기 전/후 문자의 길이가 같아야 한다.
obj = 'python'
before = 'thon'
after = 'zzzz'
sen = obj.maketrans(before, after)
print(sen)
print(obj.translate(sen))

# ● partition(separator)
# - 첫번째 조건이 발견되었을시 그것을 기준으로 나눈뒤 해당값만을 출력
result = 'python is powerful'.partition('is')
print(result)

# ● replace(old, new, [count])
result = 'python is powerful'.replace('p', 'P')
print(result)
result = 'python is powerful'.replace('p', 'P', 1)
print(result)

# ● rfind(separator)
# - 뒤에서부터 문자열을 찾음
result = 'python is powerful'.rfind('p')
print(result)
result = 'python is powerful'.rfind('p', 0, 9)
print(result) # 'python is p' 에서부터 뒤에서 'p'를 찾음
result = 'python is powerful'.rfind('pa')
print(result)

# ● rindex(keyword, [start, [end]])
result = 'python is powerful'.rindex('p')
print(result)
# result = 'python is powerful'.rindex('pa')  # 없으면 Error 발생
# print(result)

# ● rpartition(separator)
result = 'python is powerful'.rpartition('p')
print(result)

# ● rsplit([separator, [maxsplit]])
result = 'python is powerful'.rsplit()
print(result)
result = 'python is powerful'.rsplit(' ', 1)
print(result)

# ● split([separator, [maxsplit]])
result = 'python is powerful'.split()
print(result)
result = 'python is powerful'.split(' ', 1)
print(result)

# ● splitlines([keep])
result = 'python\r\nis\npowerful'.splitlines()
print(result)
result = 'python\r\nis\npowerful'.splitlines(True)
print(result)

# ● startswith(prefix, [start, [end]])
result = 'python is powerful'.startswith('py')
print(result)
result = 'python is powerful'.startswith('py', 5)
print(result)
result = 'python is powerful'.startswith('n', 5)
print(result)
result = 'python is powerful'.startswith('py', 0, 5)
print(result)
result = 'python is powerful'.startswith(('p', 'm'))
print(result)

# ● swapcase()
result = 'Python3.2'.swapcase()
print(result)

# ● title()
result = 'python is powerful'.title()
print(result)

# ● upper()
result = 'Python3.2'.upper()
print(result)

