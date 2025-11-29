import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "24tec2csic012@vgu.ac.in"
APP_PASSWORD = "xewy akvk evkv pbqx"
RECEIVER = "kachulil644@gmail.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Hello for python ...."
msg.set_content("This email was shared by Lilli sharma.")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)