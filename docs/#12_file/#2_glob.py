#-- glob
# ● glob(path)
#   - Path 경로에 대응되는 모든 파일 및 디렉터리의 리스트를 반환
#   - 경로를 주는 방식에 따라 절대 경로로 결과가 나오게 할 수도 있음
import glob
print(glob.glob('/Users/soryong/workspace/project/guide/learning-python/*'))
print(glob.glob('*'))
print(glob.glob('*.md'))
print(glob.glob('tes?.txt'))

# ● iglob(path)
#   - glob과 동일한 동작을 수행하지만, 리스트로 결과를 반환하는 것이 아니라 이터레이터를 반환함
print(glob.iglob('*'))
for i in glob.iglob('*'):
  print(i)