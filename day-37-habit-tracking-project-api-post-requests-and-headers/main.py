import requests
from datetime import date

# Today
today = date.today()
formatted_today = today.strftime("%Y%m%d")
# Set a day
certain_day = date(year=2022, month=12, day=1)
formatted_some_day = certain_day.strftime("%Y%m%d")

USERNAME = "<username>"
TOKEN = "<token>"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creates USER
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_parameters['username']}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Days with SQL",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}

# Creates GRAPH
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
add_pixel_config = {
    "date": formatted_today,
    "quantity": "1"
}

# Adds PIXEL
# response = requests.post(url=add_pixel_endpoint, json=add_pixel_config, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}/{formatted_today}"
update_pixel_config = {
    "quantity": "1",
}

# Updates PIXEL
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# Deletes PIXEL
# delete_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}/{formatted_some_day}"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
