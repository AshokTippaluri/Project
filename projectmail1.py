from email import message
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587) #we are using gmail server for this server port is 587

server.starttls()  #to encryption the message we are using tls (transport layer service)

server.login('sender@gmail.com', 'password')

subject = 'This mail sent from smtp'
body = '3rd mail sent throught SMTP protocol by using python '

Message1 = f'Subject: {subject}\n\n{body}'

server.sendmail('sender@gmail.com', 'reciver@gmail.com', Message1)

print('Mail Sent')
