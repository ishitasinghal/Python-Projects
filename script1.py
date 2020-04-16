#!/usr/bin/python
import smtplib

sender = '500060649@stu.upes.ac.in'
receivers = ['ishitasinghal08@gmail.com']

message = """From: From Person <500060649@stu.upes.ac.in>
To: To Person <ishitasinghal08@gmail.com>

Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except (OSError, smtplib.SMTPException) as e:
    print("Error: unable to send email")