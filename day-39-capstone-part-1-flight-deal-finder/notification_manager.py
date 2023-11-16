from twilio.rest import Client


class NotificationManager:

    def __init__(self, twillio_number, account_sid, auth_token):
        self.twillio_number = twillio_number
        self.account_sid = account_sid
        self.auth_token = auth_token

    def send_sms_notification(self, receiver_number, text_message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=text_message,
            from_=self.twillio_number,
            to=receiver_number
        )
