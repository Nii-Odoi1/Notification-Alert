#!/usr/bin/python3
# -*- coding: utf-8 -*-

# before running the script, enable less secure apps from this link --> https://myaccount.google.com/lesssecureapps

import smtplib
from email.message import EmailMessage

# This variable is to mimic the number of sms sent in a day. Ideally, it would come from an API tracking it
messages_a_day = int(input("How many SMS messages were sent today: "))

thresHold = 45000

if(messages_a_day < thresHold):
    # send an alert email
    # replace <email> with your actual email and <password> with the email's actual password
    Email = "<email>"
    Pass = "<password>"

    msg = EmailMessage()
    msg['Subject'] = 'SMS Notification Alert'
    msg['From'] = Email
    
    # replace <recipient email> with any accessible email
    msg['To'] = '<recipient email>'
    msg.set_content('Few SMSs have been sent today. Only ' + str(messages_a_day) + ' sms has been sent.')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Email, Pass)
        smtp.send_message(msg)

else:
    print("A minimum of 45000 SMS messages threshold met")