import os
import requests

SHEETY_API_TOKEN = f"Bearer SOC_Q!@W#E$R%TY&U*I(O)P"
SHEETY_API_ENDPOINT = "https://api.sheety.co/60e2c0d8e5d9419cbbffa0d118002c9c/wantedFlights/prices"
SHEETY_HEADERS = {
    'Authorization': SHEETY_API_TOKEN
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_API_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_API_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=SHEETY_HEADERS,
            )
            print(response.text)
