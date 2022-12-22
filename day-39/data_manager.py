import requests


class DataManager:

    def __init__(self, api_endpoint: str, api_headers: dict):
        self.endpoint = api_endpoint
        self.headers = api_headers

    def get_request(self):
        get_response = requests.get(url=self.endpoint, headers=self.headers)
        get_response.raise_for_status()
        return get_response.json()

    def post_request(self, query: dict):
        post_response = requests.post(url=self.endpoint, json=query, headers=self.headers)
        post_response.raise_for_status()
        return post_response.json()

    def put_request(self, row_number: str, query: dict):
        put_request = requests.put(url=f"{self.endpoint}/{row_number}", json=query, headers=self.headers)
        put_request.raise_for_status()
        return put_request.json()

    def delete_request(self, row_number: str):
        delete_request = requests.delete(url=f"{self.endpoint}/{row_number}", headers=self.headers)
        delete_request.raise_for_status()
