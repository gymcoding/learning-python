#-- os module

# ● os.getcwd()
#   - getcwd() 함수는 현재 작업 디렉터리의 위치를 가져올 때 쓰임
from os import (
  getcwd, chdir, access,
  F_OK, W_OK, X_OK, R_OK,
  listdir, mkdir, makedirs,
  remove, unlink, rmdir,
  removedirs, rename, stat,
  utime, walk, pipe, fdopen,
  popen, system, execl, execv, execle
)
print(getcwd())

# ● os.chdir(path)
#   - chdir() 함수는 현재 작업 디렉터리 위치를 변경함
print(chdir('/Users/soryong/workspace/project/guide/learning-python'))
print(getcwd())

# ● os.access(path, mode)
#   - 입력받은 <path>에 대해서 <mode>에 해당하는 작업이 가능한 지의 여부를 반환
print('F_OK: ', F_OK)
print('W_OK: ', W_OK)
print('X_OK: ', X_OK)
print('R_OK: ', R_OK)
print(access('.', F_OK))
print(access('.', W_OK | X_OK | R_OK))

# ● os.listdir(path)
#   - 해당 경로(path)에 존재하는 파일과 디렉터리들의 리스트를 반환
print(listdir('.'))

# ● os.mkdir(path, [, mode])
#   - <path>에 해당하는 디렉터리를 생성
try:
  mkdir('docs/#14_os/test1')
  print(listdir('docs/#14_os/'))
except Exception as e:
  print('e: ', e.args[1])

# ● os.makedirs(path, [, mode])
#   - 인자로 전달된 디렉터리를 재귀적으로 생성
try:
  makedirs('docs/#14_os/test1/recursive1/recursive2/recursive3')
  print(listdir('docs/#14_os/test1/recursive1/recursive2'))
except Exception as e:
  print('e: ', e.args[1])

# ● os.remove(path), os.unlink(path)
#   - 파일을 삭제
try:
  remove('docs/#14_os/test1/recursive1/recursive2/recursive3')
  unlink('docs/#14_os/test1/recursive1/recursive2/')
except Exception as e:
  print('e: ', e.args[1])

# ● os.rmdir(path)
#   - 디렉터리를 삭제
try:
  rmdir('docs/#14_os/test1/recursive1/recursive2/recursive3')
  rmdir('docs/#14_os/test1/recursive1/recursive2')
except Exception as e:
  print('e: ', e.args[1])

# ● os.removedirs(path)
#   - 디렉터리를 순차적으로 삭제
try:
  removedirs('docs/#14_os/test1/recursive1')
except Exception as e:
  print('e: ', e.args[1])

# ● os.rename(src, dst)
#   - src를 dst로 이름을 변경하거나 이동
try:
  rename('test.txt', 'renamed.txt')
except Exception as e:
  print('e: ', e.args[1])

# ● os.utime(path, times)
#   - 경로에 해당하는 파일에 대해 액세스 시간(access time)과 수정 시간(modified time)을 <times>로 수정
result = stat('test_renames/moved.txt')
print('stat')
print(result)
result = utime('test_renames/moved.txt', None)
print('utime')
print(result)
result = stat('test_renames/moved.txt')
print(result)

# ● walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
#   - top으로 지정된 디렉터리를 순회하며 경로, 디렉터리 명을 순차적으로 반환
for path, dirs, files in walk('test_renames'):
  print(path, dirs, files)

# ● pipe()
#   - 파이프를 생성
# pipe()(5, 6) # Error 확인

# ● fdopen(fd[, mode[, bufsize]])
#   - 파일 디스크립터를 이용해 파일 객체를 생성
r, w = pipe()
rd = fdopen(r)
print('rd')
print(rd)

# ● popen(command[, mode[, bufsize]])
#   - 인자로 전달된 command를 수행하며 파이프를 생성
p = popen('ls', 'r')
print('ls')
print(p.read())

# ● system(command)
#   - <command>를 실행하며, 성공한 경우 0을 반환
print(system('ls -al'))

# ● startfile(path, [, operation])
#   - <path>를 os에서 지정된 프로그램으로 실행
# Error startfile 함수가 없음

# ● execl(path, arg0, arg1, ...)
#   - 현재 프로세스에서 새로운 프로그램을 수행
# execv('python', ('python', '-v'))