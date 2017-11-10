#! /bin/python

import smtplib


print('**** MAKE SURE YOU ARE USING A GMAIL ****')
print('enter your email address')

email = input()

print('enter your password')

password = input()

print('who do you want to send the email to?')

send_to =  input()

print('subject line')

subject = "Subject: " + input() + "\n"  #this is funky for formatting purposes 

print('enter the body of your email')

body = input()

smtp0bj = smtplib.SMTP('smtp.gmail.com', 587) #googles smtp server 

smtp0bj.ehlo() 

smtp0bj.starttls()

smtp0bj.login(email, password) 


smtp0bj.sendmail(email, send_to, subject +  body)

smtp0bj.quit()
