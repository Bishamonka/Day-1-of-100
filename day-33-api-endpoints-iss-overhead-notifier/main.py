# This program gets current ISS position via API and compares it to users current location.
# If ISS is close, and it's currently night in the area — sends email to 'Look up!'

import requests
from datetime import datetime
import smtplib

MY_LAT = 48.922634
MY_LONG = 24.711117
MY_EMAIL = ""
MY_PASSWORD = ""

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:
    ISS_is_visible = True
else:
    ISS_is_visible = False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if sunrise < time_now.hour < sunset:
    is_night_now = True
else:
    is_night_now = False


if ISS_is_visible and is_night_now:
    print("Look up! The ISS is above you!")
    pass  # Since Email credentials are empty, I've used 'pass' to prevent ErrorMessages
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look up!\n\nThe ISS is above you!"
    )
elif ISS_is_visible and not is_night_now:
    print("ISS is near, if only it was night now, you could see it")
else:
    print("ISS is currently somewhere else, and not visible yet")

