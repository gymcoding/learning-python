#-- 간단한 FTP 프로그램
# ● FTP로 서버에 접근해 파일 리스트를 가져오는 프로그램
from ftplib import FTP
ftp = FTP('ftp.cwi.nl')
ftp.login()
ftp.retrlines('LIST')