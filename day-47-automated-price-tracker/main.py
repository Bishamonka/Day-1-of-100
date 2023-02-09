import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import time

amazon_url = "https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/ref=sr_1_3?keywords=rasberry%2Bpi%2B4%2B&qid=1674735045&sprefix=rasbe%2Caps%2C247&sr=8-3&th=1"
alert_price = 150

code_is_working = True

while code_is_working:

    current_time = (datetime.now()).strftime("%H:%M")

    # Reduce resources consuming by running if/else statement only every 15 seconds.
    # By running every 15 seconds gives 4 chances to meet condition.

    time.sleep(15)

    if current_time == "17:16":

        headers = {
            "Accept-Language": "uk,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        }
        response = requests.get(url=amazon_url, headers=headers)
        soup = response.text
        soup = bs(soup, "html.parser")

        current_price_whole = soup.find(name="span", class_="a-price-whole").text
        current_price_decimal = soup.find(name="span", class_="a-price-fraction").text

        current_price = float(current_price_whole + current_price_decimal)
        print(f"\nIt's {current_time} now.\n")

        if current_price < alert_price:
            print("SALE!!! Its time to buy!")
            print(f"Wanted price: ${alert_price}\nCurrent price on website: ${current_price}")
            diff = alert_price - current_price
            print(f"${diff:.2f} less!")
        else:
            print(f"No good price for today.\nWanted price: ${alert_price}\nCurrent price on website: ${current_price}")

        # Since f.e. '15:00' is only once per 24 hours day, setting 'if else' on that time is no problem.
        # Not specifying seconds gives 1 minute buffer for Python code to run.
        # To prevent multiple runs of code per that specific minute-period, we 'pause' code for 60 seconds.

        time.sleep(60)

    else:
        pass

