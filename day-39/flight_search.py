import requests


class FlightSearch:

    def __init__(
            self,
            kiwi_search_api_endpoint: str,
            kiwi_api_headers: dict,
            fly_from: str,
            fly_to: list,
            date_from: str,
            date_to: str,
            curr=str,
            ):

        self.endpoint = kiwi_search_api_endpoint
        self.headers = kiwi_api_headers
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.date_from = date_from
        self.date_to = date_to
        self.curr = curr

    def get_the_cheapest_flight_prices(self):
        cheapest_prices = []
        for iata_code in self.fly_to:
            parameters = {
                "fly_from": self.fly_from,
                "fly_to": iata_code,
                "date_from": self.date_from,
                "date_to": self.date_to,
                "curr": self.curr
            }
            found_flights = requests.get(url=self.endpoint, params=parameters, headers=self.headers)
            cheapest_prices.append(found_flights.json()["data"][0]["price"])
        return cheapest_prices
