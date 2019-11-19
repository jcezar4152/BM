#Importando Bibliotecas - Não necessário instalação via PIP pois são nativas do Python!
import smtplib # Biblioteca para utilizar o protocolo SMTP no envio de Emails
import email.mime.text # Função para envio de email em Texto Básico
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#def hahaha(assunto, mensagem, to_addrs):
# INICIO - Autenticação de Email - host e port padrão do GMAIL
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
username = 'blackmambabot1@gmail.com'
password = '123456bd'
# FIM - Autenticação de Email

# INICIO - Definição das váriavéis do envio de Email
from_addr = 'blackmambabot1@gmail.com'
to_addrs = 'sabrinarcmariano@gmail.com' # passou a ser informado no SELECT feito em BM_raspagem
message = MIMEMultipart()
message['subject'] = "IMAGEM BLACKMAMBA - COMPRA A AÇÃO LOGO CARA TA ESPERANDO OQUE"
message['from'] = from_addr
message['bcc'] = to_addrs #', '.join(to_addrs).
filename='diario.png'
attachment  =open(filename,'rb')
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
message.attach(part)
# FIM - Definição do Email

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port) # Realiza conexão segura com o servidor do Email
server.login(username, password) # Interação com o servidor: Insere Usuario e Senha
server.sendmail(from_addr, to_addrs, message.as_string()) # Interação com o servidor: Envia o Email
server.quit() # Fecha conexão com o servidor do Email

print("E-mail enviado com sucesso!")
