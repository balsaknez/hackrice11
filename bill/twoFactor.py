import random
import smtplib
from getpass import getpass
from email.mime.text import MIMEText

dict = {}

def send_mail(receiver):
    sender = 'cssaphackrice@gmail.com'

    code = random.randint(100000, 999999)
    content = "Your authentication code is " + str(code)

    msg = MIMEText(content)
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = 'Authentication code'

    smtp_server_name = 'smtp.gmail.com'
    # port = '465' # for secure messages
    port = '587'  # for normal messages

    if port == '465':
        server = smtplib.SMTP_SSL('{}:{}'.format(smtp_server_name, port))
    else:
        server = smtplib.SMTP('{}:{}'.format(smtp_server_name, port))
        server.starttls()  # this is for secure reason

    server.login(sender, "Asdfasdf22!")
    server.send_message(msg)
    server.quit()

    dict[receiver] = code
    return str(code)


def authenticate(receiver, code):
    if code == dict.get(receiver, None):
        dict[receiver] = None
        return True
    return False

send_mail("andrej.jakovljevic2000@gmail.com")

# def check(time):
#   if time - time2 > 0:
#     return False
#   return True
