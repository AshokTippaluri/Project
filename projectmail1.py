import smtplib
from email.message import EmailMessage

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login('sender@gmail.com', 'password')
message1 = EmailMessage()
message1['Subject'] = 'This mail sent from smtp'
message1['From'] = 'sender5@gmail.com'
message1['To'] = 'reciver@gmail.com'
message1.set_content('This mail is sent by python script by using SMTP and emailmessage. \n\nRegards,\nAshok')

server.send_message(message1)

print('Mail Sent')
