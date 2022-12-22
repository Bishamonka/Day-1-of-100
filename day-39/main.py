import os
import time
from datetime import date
from dateutil.relativedelta import relativedelta

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


# SHEETY API Constants
SHEETY_API_TOKEN = f"Bearer {os.environ['sheety_token']}"
SHEETY_API_ENDPOINT = "https://api.sheety.co/6d0451f4751988694154fdbc58388272/wantedFlights/flights"
SHEETY_HEADERS = {
    'Authorization': SHEETY_API_TOKEN
}
# KIWI API Constants
KIWI_API_TOKEN = os.environ['kiwi_token']
KIWI_API_ENDPOINT = "https://api.tequila.kiwi.com"
KIWI_HEADERS = {
    "apikey": KIWI_API_TOKEN,
}
KIWI_LOCATIONS_API_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
KIWI_SEARCH_API_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"

# TWILLIO API Constants
TWILLIO_ACCOUNT_SID = os.environ['twillio_sid']
TWILLIO_AUTH_TOKEN = os.environ['twillio_token']
TWILLIO_SENDER_NUMBER = os.environ['twillio_sender_number']
TWILLIO_RECEIVER_NUMBER = os.environ['twillio_receiver_number']


departure_city = "London"
today = date.today().strftime("%d/%m/%Y")
six_months_after_today = (date.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")
currency = "USD"


sheety_requests = DataManager(SHEETY_API_ENDPOINT, SHEETY_HEADERS)
data = sheety_requests.get_request()

sheety_data = FlightData(KIWI_LOCATIONS_API_ENDPOINT, KIWI_HEADERS, sheety_requests, data)
sheety_data.fill_in_iata_codes()

twillio_notifications = NotificationManager(
    account_sid=TWILLIO_ACCOUNT_SID,
    auth_token=TWILLIO_AUTH_TOKEN,
    twillio_number=TWILLIO_SENDER_NUMBER
)


cities_list = sheety_data.get_cities_list()
iata_codes_list = sheety_data.get_cities_iata_codes()
usually_low_prices = sheety_data.get_usually_low_prices()
FS = FlightSearch(
    kiwi_search_api_endpoint=KIWI_SEARCH_API_ENDPOINT,
    kiwi_api_headers=KIWI_HEADERS,
    fly_from=sheety_data.get_iata_code(departure_city),
    fly_to=iata_codes_list,
    date_from=today,
    date_to=six_months_after_today,
    curr=currency
)
current_cheapest_ticket_prices = FS.get_the_cheapest_flight_prices()


wanted_flights_dict = {key: value for (key, value) in zip(iata_codes_list, usually_low_prices)}
is_cheap_tickets = {}
row = 0
for tupple in list(wanted_flights_dict.items()):
    if tupple[1] > current_cheapest_ticket_prices[row]:
        is_cheap_tickets.update({tupple[0]: True})
        row += 1
    else:
        is_cheap_tickets.update({tupple[0]: False})
        row += 1


index = 0
for value in is_cheap_tickets.values():
    time.sleep(3)  # 3 secs latency between requests to prevent missing notifications
    if value == True:
        hot_price = current_cheapest_ticket_prices[index]
        fly_from_city = departure_city
        fly_from_iata_code = FS.fly_from
        destination_city = cities_list[index]
        destination_city_code = iata_codes_list[index]
        date_from = FS.date_from
        date_to = FS.date_to

        message = (f"Hot price alert! Only ${hot_price} to fly from {fly_from_city} — {fly_from_iata_code} "
                   f"to {destination_city} — {destination_city_code}, from {date_from} to {date_to}.")

        # Sends notifications to a phone
        twillio_notifications.send_sms_notification(
            receiver_number=TWILLIO_RECEIVER_NUMBER,
            text_message=message
        )
        # Prints notifications copies to terminal
        print(message)

    if index < len(cities_list):
        index += 1
