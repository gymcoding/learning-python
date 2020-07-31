#-- os.path
# ● abspath(path) - 절대 경로를 반환
import os
print(os.path.abspath('tmp'))

# ● basename(path) - 입력받은 경로의 기본 이름을 반환
print(os.path.basename('/Users/soryong/workspace/project/guide/learning-python/tmp'))

# ● dirname(path) - 입력받은 파일/디렉터리의 경로를 반환
print(os.path.dirname('/Users/soryong/workspace/project/guide/learning-python/tmp'))

# ● exists(path) - 입력받은 경로가 존재하면 True를 반환하고, 존재하지 않는 경우에는 False를 반환
print(os.path.exists('/Users/soryong/workspace/project/guide/learning-python/tmp'))
print(os.path.exists('/Users/soryong/workspace/project/guide/learning-python'))

# ● expanduser(path) - 입력받은 경로안의 "~"를 현재 사용자 디렉터리의 절대 경로로 대체
print(os.path.expanduser('~/test'))
print(os.path.expanduser('~soryong/test'))

# ● expandvars(path) - path 안에 환경 변수가 있다면 확장
print(os.path.expandvars('$HOME/temp2'))
print(os.path.expandvars('$ANDROID_HOME/temp2'))
print(os.environ)

# ● getatime(path) - 입력받은 경로에 대한 최근 접근 시간을 반환
print(os.path.getatime('/Users/soryong/workspace/project/guide/learning-python'))

# ● getmtime(path) - 입력받은 경로에 대한 최근 변경 시간을 반환
print(os.path.getmtime('/Users/soryong/workspace/project/guide/learning-python'))

# ● getctime(path) - 입력받은 경로에 대한 생성 시간을 반환
print(os.path.getctime('/Users/soryong/workspace/project/guide/learning-python'))

# ● getsize(path) - 입력받은 경로에 대한 바이트 단위의 파일 크기를 반환
print(os.path.getsize('/Users/soryong/workspace/project/guide/learning-python'))

# ● isabs(path) - 경로가 절대 경로이면 True를 반환하고, 그 외의 경우에는 False를 반환
print(os.path.isabs('/Users/soryong/workspace/project/guide/learning-python'))
print(os.path.isabs('learning-python'))

# ● isfile(path)
#   - 경로가 파일인지 아닌지 검사
#   - 파일인 경우에는 True를 반환하고, 그 외의 경우에는 False를 반환
print(os.path.isfile('/Users/soryong/workspace/project/guide/learning-python/test.txt'))
print(os.path.isfile('/Users/soryong/workspace/project/guide/learning-python'))
print(os.path.isfile('/Users/soryong/workspace/project/guide/learning-python/anonymous.txt'))

# ● isdir(path)
#   - 경로가 파일인지 아닌지 검사
#   - 파일인 경우에는 True를 반환하고, 그 외의 경우에는 False를 반환
print(os.path.isdir('/Users/soryong/workspace/project/guide/learning-python/test.txt'))
print(os.path.isdir('/Users/soryong/workspace/project/guide/learning-python'))
print(os.path.isdir('/Users/soryong/workspace/project/guide/learning-python/anonymous.txt'))

# ● join(path1, [path2[,...]]) - 해당 OS 형식에 맞도록 입력받은 경로를 연결
print(os.path.join('/User', 'soryong'))
print(os.path.join('/User', '/Anonymous', 'soryong'))

# ● normcase(path) - 해당 OS에 맞도록 입력받은 경로의 문자열을 정규화함
print(os.path.normcase('/User/soryong/workspace'))
print(os.path.normcase('C:₩User₩soryong₩workspace'))  # 변하지 않음

# ● split(path) - 입력받은 경로를 디렉터리 부분과 파일 부분으로 나눔
print(os.path.split('/User/soryong'))

# ● splitdrive(path) - 입력받은 경로를 드라이브 부분과 나머지 부분으로 나눔
print(os.path.splitdrive('/User/soryong'))

# ● splitext(path) - 입력받은 경로를 확장자 부분과 그 외의 부분으로 나눔
print(os.path.splitext('/User/soryong'))



