#Importando Bibliotecas - Não necessário instalação via PIP pois são nativas do Python!
import smtplib # Biblioteca para utilizar o protocolo SMTP no envio de Emails
import email.mime.text # Função para envio de email em Texto Básico

def hahaha(assunto, mensagem, to_addrs):
# INICIO - Autenticação de Email - host e port padrão do GMAIL
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    username = 'blackmambabot1@gmail.com'
    password = '123456bd'
    # FIM - Autenticação de Email

    # INICIO - Definição das váriavéis do envio de Email
    from_addr = 'blackmambabot1@gmail.com'
    # to_addrs = ['blackmambabot1@gmail.com']
    message = email.mime.text.MIMEText(mensagem)
    message['subject'] = assunto
    message['from'] = from_addr
    message['bcc'] = to_addrs #', '.join(to_addrs).
    # FIM - Definição do Email

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port) # Realiza conexão segura com o servidor do Email
    server.login(username, password) # Interação com o servidor: Insere Usuario e Senha
    server.sendmail(from_addr, to_addrs, message.as_string()) # Interação com o servidor: Envia o Email
    server.quit() # Fecha conexão com o servidor do Email

    print("E-mail enviado com sucesso!")
