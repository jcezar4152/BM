import smtplib
import email.mime.text

smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

username = 'blackmanbabd@gmail.com'
password = '123456BD'

from_addr = 'blackmanbabd@gmail.com'
to_addrs = ['daniel.delgado.rocha@gmail.com','blackmanbabd@hotmail.com']

message = email.mime.text.MIMEText('TESTE BLACKY')
message['subject'] = 'TESTE BLACK'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()
print("Deu bom!")