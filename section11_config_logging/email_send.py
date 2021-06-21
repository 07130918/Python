import smtplib
import ssl
from email.mime.text import MIMEText

gmail_account = "tokyosato1@gmail.com"
gmail_password = "ここにパスワードを入力"
mail_to = "tokyosato1@gmail.com"

subject = "メール送信テスト"
body = "メール送信テスト"
msg = MIMEText(body, "html")
msg["Subject"] = subject
msg["To"] = mail_to
msg["From"] = gmail_account

server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
                          context=ssl.create_default_context())
server.login(gmail_account, gmail_password)
server.send_message(msg)
print("ok")
