from dotenv import load_dotenv
from email.message import EmailMessage
import os
import ssl
import smtplib

load_dotenv()
email_from = os.getenv("EMAIL_FROM")
email_password = os.getenv("EMAIL_PASSWORD")
email_smtp_server = os.getenv("EMAIL_SMTP_SERVER")
email_port_server = os.getenv("EMAIL_PORT_SERVER") 


email_to = "aurelio.mont@me.com"

email_subject = "More info"

email_content = """ Quiero mas informacion sobre tus servicios """

email_message = EmailMessage()

email_message["From"] = email_from
email_message["To"] = email_to
email_message["Subject"] = email_subject
email_message.set_content(email_content)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(email_smtp_server, email_port_server, context=context) as SMTP:
    SMTP.login(email_from, email_password)
    SMTP.sendmail(email_from, email_to, email_message.as_string())