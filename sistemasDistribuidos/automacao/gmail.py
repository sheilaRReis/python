import yagmail

user = 'sheilarreis@gmail.com'
# Senha gerada em google Account -> Segurança -> Verificação em 2 etapas -> app password
app_password = 'yzfxxezbuandcqoy' 
to = 'sheilarreis@hotmail.com'

subject = 'test subject 1'
content = ['<h1>Main e-mail title</h1><p>First paragraph</p><p>Second paragraph</p><br/><p><b>Bold text</b></p>']

with yagmail.SMTP(user, app_password) as yag:
    # Adding multiple attachments and mailing them
    yag.send(to, subject, content, attachments=['teste.txt','img.jpg'])


print('Sent email successfully')
