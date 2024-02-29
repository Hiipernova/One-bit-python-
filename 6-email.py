import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

password = open("senha", "r").read()
from_email="teste123@gmail.com"
to_email="teste123@gmail.com"
subject="Automação Planilha"
body = """
Olá. Seguem em anexo a automação da planilha
para a empreza XYZ Automação.

Qualquer dúvida estou a disposição!
"""

message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.set_content(body)
safe = ssl.create_default_context()


anexo = "test.xlsx"
#print(mime_subtype = mimetypes.guess_type(anexo)[0].split("/"))
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split("/")
with open(anexo, "rb") as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type
        subtype=mime_subtype
        filename=anexo
    )

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )