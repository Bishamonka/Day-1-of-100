import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.getenv('TWILIO_VIRTUAL_NUMBER')
TWILIO_VERIFIED_NUMBER = os.getenv('TWILIO_VERIFIED_NUMBER')

customers = ["bishamon.dev@gmail.com"]


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message):
        for customer in customers:
            my_email = os.getenv('my_email')
            password = os.getenv('password')

            msg = MIMEText(message)
            msg['Subject'] = "New Cheap Flights!"

            with smtplib.SMTP("smtp.office365.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=customer,
                    msg=msg.as_string()
                )
                print(f"Message to {customer} is sent")
