import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('sender@gmail.com', 'password')

server.sendmail('sender@gmail.com', 'reciver@gmail.com', 'This Mail sent throught SMTP server by using python')

print('Mail Sent')
