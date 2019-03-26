import smtplib
from email.mime.text import MIMEText


#smtp 인스턴스 생성 (서버url, port)
smtp = smtplib.SMTP('smtp.gmail.com', 587)

# TLS 보안 시작
smtp.starttls()

# 서버 로그인을 위해 login 함수 호출
smtp.login('flowday7@gmail.com', 'tgljwcmntiqbztpf')

# 보낼 메시지
message = MIMEText('본문 : Hello')
message['Subject'] = '제목 : 테스트'

# 메일 보내기
smtp.sendmail('flowday7@gmail.com', 'uxinsight@naver.com', message.as_string())

# 세션 종료
smtp.quit()
