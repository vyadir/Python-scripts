import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import os
import datetime

# para escribir ficheros de logs
def reporte_errores(texto):
    f = open("Errores_Ejecucion.txt", "a")
    f.write(texto)
    f.close()

# enviar correos electronicos
def sendmail(messag,subject,me,to,cc,passw,filename,serv,port):
    try:
        msg = MIMEMultipart()
        message = messag
        rcpt = cc.split(",")  + to.split(",")
        password = passw
        msg['From'] = me
        msg['To'] = to
        msg['Cc'] = cc
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(filename, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
        msg.attach(part)

        strServer = serv + ": " + port
        server = smtplib.SMTP(strServer)
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'],rcpt, msg.as_string())
        server.quit()
        
        reporte_errores(str("Email enviado correctamente a %s:" % (msg['To'])) + "\n")

   except Exception as e:
        reporte_errores("ERROR:       " + str(e) + "\n")