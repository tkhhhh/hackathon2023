from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText

def send_mail(username, passwd, recv, title, content, mail_host='smtp.qq.com', port=25, file=None):
    if file:
        msg = MIMEMultipart()

        part_text = MIMEText(content)
        msg.attach(part_text)
        part_attach1 = MIMEApplication(open('./foo.pdf', 'rb').read())
        part_attach1.add_header('Content-Disposition', 'attachment', filename=file)  # 为附件命名
        msg.attach(part_attach1)
    else:
        msg = MIMEText(content)
    msg['Subject'] = title
    msg['From'] = username
    msg['To'] = recv
    smtp = smtplib.SMTP(mail_host, port=port)
    smtp.login(username, passwd)
    smtp.sendmail(username, recv, msg.as_string())
    smtp.quit()

send_mail("626627983@qq.com", "fangxienan666", "bitfffff@163.com", "test", "test")
