import smtplib
import time
import random

from pdf import encoded

from email.header import Header
from email.mime.text import MIMEText

me = 'example@gmail.com'  # change to your email
recipients = ['example@gmail.com']  # enter recipients here


def spamEveryMinute():
    while (True):
        msg = MIMEText(encoded, 'plain', 'utf-8')

        code_ID = random.randint(0, 10000)
        msg['Subject'] = Header(
            'Read it, it"s urgent (code_ID: ' + str(code_ID) + ')', 'utf-8')
        msg['From'] = 'example@gmail.com'
        msg['To'] = ', '.join(recipients)

        s = smtplib.SMTP('smtp.gmail.com', 587) #for other services change smtp here
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login('your email here', 'your password')
        s.sendmail(me, recipients, msg.as_string())

        print(("Email sent to: " + ', '.join(recipients)))
        s.quit()
        time.sleep(.100) #change time here


spamEveryMinute()
