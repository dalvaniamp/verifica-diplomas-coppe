import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email =""
password = ""

class EmailUtils():
    @staticmethod
    def send_email(recipient):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password) 

        message = MIMEMultipart("alternative")
        message["Subject"] = "Seu diploma esta pronto"
        message["From"] = f"Aviso Diploma{email}"
        message["To"] = recipient
        message.attach(MIMEText("De acordo com o site da COPPE, o seu diploma esta pronto para retirada.", "plain"))


        server.sendmail(email, recipient, message.as_string())
        server.quit()