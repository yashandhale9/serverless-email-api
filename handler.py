import smtplib
import json
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email(event, context):
    try:
        body = json.loads(event['body'])
        receiver_email = body['receiver_email']
        subject = body['subject']
        body_text = body['body_text']

        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")

        msg = MIMEText(body_text, 'html')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        with smtplib.SMTP_SSL(os.getenv("SMTP_HOST"), int(os.getenv("SMTP_PORT"))) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully!"})
        }

    except Exception as e:
    
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
