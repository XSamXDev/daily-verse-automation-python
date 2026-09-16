import smtplib
from email.mime.text import MIMEText
from os import getenv

from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = getenv("SMTP_EMAIL")
SENDER_PASSWORD = getenv("SMTP_PASSWORD")
SMTP_SERVER = getenv("SMTP_SERVER")
SMTP_PORT = getenv("SMTP_PORT")


def send_email(body):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        msg = MIMEText(body, "html", "utf-8")
        msg["Subject"] = "📖 Verse Of The Day 📖"
        msg["From"] = SENDER_EMAIL
        msg["To"] = "connectsameer.in@gmail.com"

        server.send_message(msg)
        server.quit()

    except smtplib.SMTPException as e:
        print(f"Error: Email could not be sent. {e}")
