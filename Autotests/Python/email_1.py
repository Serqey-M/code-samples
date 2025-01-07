import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def email_(fromaddr, toaddr, mypass, body, filename):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Отчет'

    with open(filename, 'rb') as f:
        part = MIMEApplication(f.read(), Name = basename(filename))
        part['Content_Disposition'] = 'attachment; filename = "%s"' % basename(filename)
        msg.attach(part)
       
    msg.attach(MIMEText(body, 'plan'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit