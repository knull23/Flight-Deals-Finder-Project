import os
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib
load_dotenv()


class NotificationManager:
    def __init__(self):
        self.twilio_phone_no = os.environ["DB_TWILIO_PHONE_NO"]
        self.acc_sid = os.environ["DB_ACC_SID"]
        self.auth_token = os.environ["DB_AUTH_TOKEN"]
        self.your_phone_number = os.environ['DB_YOUR_PHONE_NUMBER']
        self.whatsapp_number = os.environ['DB_WHATSAPP_NUMBER']
        self.email = os.environ['DB_MY_EMAIL']
        self.password = os.environ['DB_MY_PASSWORD']
        self.client = Client(self.acc_sid, self.auth_token)
        self.connection = smtplib.SMTP(os.environ['DB_EMAIL_PROVIDER_SMTP_ADDRESS'])

    def send_sms(self, message_body):
        try:
            message = self.client.messages.create(
                from_=self.twilio_phone_no,
                body=message_body,
                to=self.your_phone_number,
            )
            print(f"Message sent: {message.sid}")
        except Exception as e:
            print(f"Failed to send message: {e}")

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject: New Low Price FLight!\n\n"
                        f"{email_body}".encode('utf-8'),
                )
