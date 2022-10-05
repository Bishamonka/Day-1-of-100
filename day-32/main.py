import random
import smtplib
import datetime as dt
import pandas as pd
from email.mime.text import MIMEText

data = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
current_month = now.month
current_day = now.day

birthday_row = data[(data['month'] == current_month) & (data['day'] == current_day)]

receiver_name = ''
receiver_email = ''

#
# If there is at least 1 row that matches conditions, then someone has a birthday today, so use that row's data
#

if not birthday_row.empty:

    receiver_info = (birthday_row.to_dict('records'))[0]
    receiver_name = receiver_info['name']
    receiver_email = receiver_info['email']

    print(f"There is a {receiver_info}'s birthday today!")

    #
    # Pick a random letter template
    #

    letter_number = random.randrange(1, 4)
    print(letter_number)
    with open(f"letter_templates/letter_{letter_number}.txt", 'r') as letter_template:
        letter_text = letter_template.read()
        new_letter = letter_text.replace('[NAME]', receiver_name)
        print(new_letter)

    #
    # Send a letter.
    # Since the sending account is on @hotmail, have to use 'MIMEText' to avoid 'blank' letters.
    #

    my_email = "example@hotmail.com"
    password = "password"

    msg = MIMEText(new_letter)
    msg['Subject'] = "Happy Birthday!"

    with smtplib.SMTP("smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_email,
            msg=msg.as_string()
        )


else:
    print("No birthdays today...")
