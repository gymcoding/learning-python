#-- 모듈 임포트 파헤치기
# ● 임포트를 할 때, 해당 모듈의 바이트 코드가 있으면 이를 임포트 함
# ● 모듈을 임포트 하면 해당 모듈의 코드가 실행
# ● 모듈이 임포트 되면 메모리에 모듈 코드가 로딩되고, 프로그램이나 파이썬 인터프리터가 끝나기 전까지 변경되지 않음

#-- 바이트 코드 (일종의 중간 파일)
# ● 모듈의 임포트를 빠르게 해주는 역할
# ● 바이트 코드가 이미 있으면: 모듈을 인터프리팅(Interpreting) 하지 않고 바로 바이트 코드 로딩
# ● 바이트 코드가 없으면: 모듈을 인터프리팅 해서 바이트 코드를 생성
# ● 바이트 코드가 생성된 모습

#-- 모듈이 메모리에 로딩 될 때
# ● 모듈의 코드가 실행 됨
print('test module')
default_value = 1
def print_default_value():
  print(default_value)

#-- 유용한 팁: 모듈이 직접 실행 혹은 다른 곳에서 임포트 되었는지를 구분해 줄 수 있는 __name__ 어트리뷰트
# ● 모듈이 임포트 되었을 때 __name__은 모듈 자기 자신의 이름
# ● 모듈이 직접 실행 되었을 때 __name__은 "__main__"
print('my module')
print(__name__)
if __name__ == '__main__':
  print('모듈을 직접 실행하셨네요')
else:
  print('임포트 하셨네요')

#-- 패키지: 모듈의 모음
# ● 파이썬의 모듈 이름 공간을 구조화 하는 한 방법
# ● 파이썬 내장 라이브ㅓ리 중 XML 패키지의 디렉처리 구조
'''
|---  __init__.py
      +---  dom
            +---  __init__.py
            +---  domreg.py
            +---  expatbuilder.py
            ...
      +---  etree
            +---  __init__.py
            +---  cElementTree.py
            ...
      +---  parsers
            +---  __init__.py
            +---  expat.py
            ...
'''

#-- __init__.py 내부
'''
__all__ = ['dom', 'parsers', 'sax', 'etree']
...
__version__ = '$Revision: 41660 $'.split()[-2:][0]
...
_MINIMUM_XMLPLUS_VERSION = (0, 8, 4)
...
try:
import _xmlplus
except ImportError:
  pass
'''

#-- 모듈 임포트 예제 - 1/2
from xml import *
print(etree)
print(dom)

import xml.dom
print(xml.dom)

#-- 모듈 임포트 예제 - 2/2
import xml.dom.minidom as minidom
parse_string = minidom.parseString('<foo><bar/></foo>')
print('parse_string: ', parse_string)

#-- 패키지 사용 시 주의점
import xml
print(xml)
print(xml.dom)

#-- 패키지 안에서 패키지 안의 모듈
'''
sound/
  +---  __init__.py
        +---  formats/
              +---  __init__.py
              +---  wavread.py
              +---  auread.py
              +---  auwrite.py
              ...
        +---  effects/
              +---  __init__.py
              +---  echo.py
              ...
        +---  filters/
              +---  __init__.py
              +---  equalizer.py
              ...
'''