#-- 정규표현식
# ● 특정한 규칙을 가진 문자열을 표현하는데 사용되는 형식 언어
# ● 주어진 패턴으로 문자열을 검색/치환하는데 사용
# ● vi, grep 등 프로그램에서 널리 사용

#-- 정규표현식 문법
# ● 문자나 문자의 패턴을 나타내기 위한 특수 문자들
#   1)  "."     - 개행 문자를 제외한 1자를 의미
#   2)  "^"     - 문자열의 시작
#   3)  "$"     - 문자열의 종료
#   4)  "[]"    - 문자의 집합
#   5)  "|"     - OR
#   6)  "()"    - 괄호 안의 정규식을 그룹으로 만듦
#   7)  "*"     - 문자가 0회 이상 반복
#   8)  "+"     - 문자가 1회 이상 반복
#   9)  "?"     - 문자가 0 혹은 1회 반복
#   10) "{m}"   - 문자가 m회 반복
#   11) "{m,n}" - 문자가 m회 부터 n회 까지 반복되는 모든 경우
#   12) "{m,}"  - 문자가 m회 부터 무한 반복되는 모든 경우

#-- 정규표현식 예제
# 1) 'app.e'      - 'apple', 'appLe', 'app-e', 'app4e', 'app e'이 매치됩니다.
# 2) '^app'       - 'apple and orange'는 매치되지만, 'orange and apple'은 매치되지 않습니다.
# 3) 'ple$'       - 'orange and apple'은 매치되지만, 'apple and orange'는 매치되지 않습니다.  
# 4) 'appl[a-z]'  - 'apple', 'applz'와 같이 가장 마지막에 소문자가 오는 경우는 매치되지만, 'applE', 'appl4', 'appl_', 'appl '와 같은 경우는 매치되지 않습니다.  
# 5) 'appl[^a-z]' - 위의 경우와 반대로 마지막에 소문자가 오는 경우를 제외한 모든 경우에 매치됩니다.
# 6) 'apple|E'    - 'apple', 'applE'와 매치됩니다.

#-- Escape 문자열
# 1) \w - 밑줄과 표현 가능한 문자
# 2) \W - 밑줄과 표현 가능한 문자를 제외한 나머지 문자 
# 3) \d - 0-9를 포함하는 모든 숫자
# 4) \D - 숫자를 제외한 모든 문자 
# 5) \s - 공백 문자
# 6) \S - 공백 문자를 제외한 모든 문자
# 7) \\ - 역슬래쉬(\) 문자 자체를 의미 

#-- re 모듈
# ● search(pattern, string[, flags])
#   - string 전체에 대해서 pattern이 존재하는지 검사하여 MatchObject 인스턴스를 반환
# ● match(pattern, string[, flags])
#   - string 시작부분부터 pattern이 존자하는지 검사하여 MatchObject 인스턴스를 반환
# ● split(pattern, string[, maxsplit=0])
#   - pattern을 구분자로 string을 분리하여 리스트로 반환함
# ● findall(pattern, string[, flags])
#   - string에서 pattern과 매치되는 모든 경우를 찾아 리스트로 반환
# ● sub(pattern, repl, string[, count])
#   - string에서 pattern과 일치하는 부분에 대하여 repl로 교체하여 결과 문자열을 반환

#-- re.match, re.search 예제
import re

match_object = re.match('[0-9]*th', '35th')  # 결과로 MatchObject를 반환합니다.
print(match_object)

result = bool(re.match('[0-9]*th', '35th'))  # boolean으로 검색 결과 확인 가능합니다.
print(result)
result = bool(re.search('[0-9]*th', '35th'))  # boolean으로 검색 결과 확인 가능합니다.
print(result)
result = bool(re.match('ap', 'This is an apple'))  # 문자열의 시작부터 검색합니다.
print(result)
result = bool(re.search('[0-9]*th', 'This is'))  # 문자열 전체에 대해서 검색합니다.
print(result)

#-- re.findall 예제
result = re.findall(r"app\w*", "application orange apple banana")  # 매치되는 문자열이 있는 경우
print(result)
result = re.findall(r"king\w*", "application orange apple banana") # 매치되는 문자
print(result)

#-- re.sub 예제
result = re.sub('-', '', '901225-1234567') # 주민등록번호 형식을 변경합니다.
print(result)
result = re.sub(r"[:,|\s]", ',', 'Apple:Orange Banana|Tomato')  # 필드 구분자를 통일합니다.
print(result)