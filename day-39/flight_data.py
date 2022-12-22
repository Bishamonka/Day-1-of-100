import requests


class FlightData:

    def __init__(self, kiwi_locations_api_endpoint: str, kiwi_api_headers: dict, sheety_requests, data):
        self.endpoint = kiwi_locations_api_endpoint
        self.headers = kiwi_api_headers
        self.sheety_data = data
        self.sheety_requests = sheety_requests

    def get_iata_code(self, city_name: str) -> str:
        """
        Returns corresponding IATA Code using 'Tequila Kiwi Locations API'
        """
        location_query = {
            "term": city_name,
        }
        response = requests.get(url=self.endpoint, params=location_query, headers=self.headers)
        return response.json()['locations'][0]['code']

    def fill_in_iata_codes(self):
        """
        Loops through 'city names' in provided Excel file (using Sheety API)
        and finds corresponding IATA Codes using 'get_iata_code()' function,
        then via PUT request writes them in the corresponding column.
        """
        current_row = 1
        for row in self.sheety_data["flights"]:
            city_name = row["city"]
            city_code = self.get_iata_code(city_name)
            updated_row_data = {
                "flight": {
                    "iataCode": city_code,
                }
            }
            current_row += 1
            self.sheety_requests.put_request(current_row, updated_row_data)

    def get_cities_list(self):
        cities_list = []
        for row in self.sheety_data["flights"]:
            city_name = row["city"]
            cities_list.append(city_name)
        return cities_list

    def get_usually_low_prices(self):
        usually_low_prices = []
        for line in self.sheety_data["flights"]:
            usually_low_prices.append(line["lowestPrice"])
        return usually_low_prices

    def get_cities_iata_codes(self):
        iata_codes = []
        for line in self.sheety_data["flights"]:
            iata_codes.append(line["iataCode"])
        return iata_codes
