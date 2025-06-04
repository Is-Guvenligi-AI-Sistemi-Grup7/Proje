# services/mailer.py
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email, subject, html_content):
    try:
        sg = SendGridAPIClient(api_key=os.getenv("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"))
        from_email = os.getenv("yalcinhalimebuse@gmail.com")
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content
        )
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        print(f"SendGrid Hatası: {e}")
        return None
