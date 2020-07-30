#-- pickle - 쓰기
# ● pickle 모듈의 dump함수를 사용하면, colors를 쉽게 파일에 저장 가능
colors = ['red', 'green', 'black']
import pickle
f = open('colors', 'wb')
pickle.dump(colors, f)
f.close()

#-- pickle - 읽기
# ● colors를 삭제한 후, load 함수를 이용해서 리스트를 읽어 들임
#   - pickle로 파일에 쓰거나 읽을 때는 반드시 바이너리 모드로 파일을 열어야함
del colors
f = open('colors', 'rb')
colors = pickle.load(f)
f.close()
print(colors)

#-- pickle - 사용자 정의 클래스
# ● pickle로 저장할 수 있는 대상은 파이썬 객체라면 거의 모두 가능
# ● 기본 자료형은 물론이고 사용자가 정의한 클래스 객체도 pickle이 가능
class test:
  var = None
a = test()
a.var = 'Test'
f = open('test', 'wb')
pickle.dump(a, f)
f.close()
f = open('test', 'rb')
b = pickle.load(f)
f.close()
print(b.var)

